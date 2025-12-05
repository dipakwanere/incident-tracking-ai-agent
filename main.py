import time, json, os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from api_simulation import create_incident_ticket

# --- 1) Load Logs & Create Embeddings ---
with open("logs/incident_logs.txt") as f:
    logs = f.read()

splitter = RecursiveCharacterTextSplitter(chunk_size=500)
log_chunks = splitter.split_text(logs)

db = Chroma.from_texts(
    log_chunks, embedding=OpenAIEmbeddings(), persist_directory="vector_store"
)

# --- 2) Agent ---
llm = ChatOpenAI(model="gpt-4o-mini")  # free tier friendly

PRIMARY_PROMPT = """
You are an AI Incident Triage Agent.
Analyze logs and identify root cause, severity & fix steps.
If unsure, respond with "low_confidence" only.
"""

FALLBACK_PROMPT = """
You are a Senior SRE Analyst.
Provide a deeper root cause analysis + action steps + impact radius.
"""


def analyze(query):
    start = time.time()
    context = db.similarity_search(query, k=3)
    ctx = "\n".join([c.page_content for c in context])

    response = llm.invoke(
        [
            {"role": "system", "content": PRIMARY_PROMPT},
            {"role": "user", "content": f"{query}\n\nLogs:\n{ctx}"},
        ]
    ).content

    # Fallback if uncertain
    if "low_confidence" in response or len(response) < 50:
        response = llm.invoke(
            [
                {"role": "system", "content": FALLBACK_PROMPT},
                {"role": "user", "content": f"{query}\n\nLogs:\n{ctx}"},
            ]
        ).content

    latency = round(time.time() - start, 3)

    # Auto-ticket creation
    if "critical" in response.lower() or "severity high" in response.lower():
        ticket = create_incident_ticket(query, "HIGH")
        response += f"\n\n🚨 Auto Ticket Triggered → {ticket['ticket_id']}"

    # Logging / Observability
    with open("agent_run_log.txt", "a") as log:
        log.write(f"\nQuery:{query}\nLatency:{latency}s\nResponse:{response}\n{'-'*60}")

    print("🔍 Response:\n", response)
    print("\n📈 Latency:", latency, "seconds")


query = input("\nAsk something (e.g., why CPU spike?): ")
analyze(query)
