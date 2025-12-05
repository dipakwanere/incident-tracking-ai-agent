# Incident Tracking AI Agent

Lightweight incident-tracking AI assistant project.

Overview

This repository contains a minimal agent for tracking and summarizing incidents. The project is prepared for containerized deployment and CI/CD to Render via GitHub Actions.

# AI Incident Triage Agent with RAG + LLM + Observability

This is a lightweight but production-relevant AI Agent for log analysis, incident investigation & RCA (Root Cause Analysis). It mimics real-world AIOps + LLMOps + agentic workflows used in enterprise environments.

Key capabilities:

- Reading multiple log files
- Embedding logs and storing vectors in ChromaDB
- Semantic retrieval (RAG) for log context
- LLM-driven RCA with a fallback prompt on low confidence
- Auto ticket creation via a simulated API
- Observability (latency and agent run logs)
- Easy to extend to LangGraph / CrewAI / AutoGen

🔥 Why this project is valuable

**Prompt engineering & tuning:** Multi-stage agent responses with fallback & escalation

**AI Pipeline triaging:** Detects uncertainty → reprocesses → improves answer quality

**Vector DB usage:** Logs indexed as embeddings → semantic retrieval

**AIOps simulation:** Reads system logs, finds issues, classifies failures

**Tool & memory integration:** Store, retrieve, escalate incidents intelligently

**Observability:** Logs execution & latency similar to production AI pipelines

Ideal for interviews and demos for LLMOps, GenAI, MLOps & AIOps roles.

## Architecture

```
				┌─────────────────────┐
				│ Incident Log Files  │
				└─────────┬───────────┘
						  ↓
			 Chunk + Embed with OpenAI
						  ↓
				 Chroma Vector DB
						  ↓
			   LLM Agent (Primary Prompt)
						  ↓
		If uncertain → Fallback Deep RCA Prompt
						  ↓
		 ┌───────────── Result ──────────────┐
		 │ Root Cause | Severity | Fix Steps │
		 └───────────────────────────────────┘
						  ↓
	  Critical? → Auto Create Incident Ticket
						  ↓
		   Observability Logs + Latency Store
```

## Project Structure

```
incident-tracking-ai-agent/
│── main.py
│── api_simulation.py
│── requirements.txt
│── agent_run_log.txt         (auto-generated)
│── /logs/                    (Add multiple log .txt/.log files here)
│   ├── sample1.txt
│   ├── sample2.log
│── /vector_store/            (auto-created by Chroma)
│── README.md
```

## Features

- **Semantic log analysis via embeddings:** ✔
- **Supports multiple log files (.txt/.log):** ✔
- **Auto RCA generation:** ✔
- **Critical → auto-creates simulated ticket:** ✔
- **Self-healing fallback prompt:** ✔
- **Observability + latency tracking:** ✔
- **Extendable to LangGraph, CrewAI, AutoGen:** 🔥

## Getting Started

1. Clone the repository

```powershell
git clone https://github.com/<your-username>/incident-tracking-ai-agent.git
cd incident-tracking-ai-agent
```

2. Create environment & install dependencies

Windows (PowerShell):

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

Linux / macOS:

```bash
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your OpenAI API key

```
OPENAI_API_KEY="your_openai_key"
```

4. Add your log files

Place one or more files inside the `logs/` folder. Example:

```
logs/
├── server_cpu_spike.txt
├── kubernetes_restarts.log
├── payment_gateway_timeout.txt
```

5. Run the agent

```powershell
python main.py
```

When prompted, type queries like:

- `What caused CPU spike yesterday?`
- `Why was DB latency high?`
- `Which service is failing repeatedly?`

## Sample Output

```
🔍 Final Response:
Root cause: Connection pool exhaustion → DB latency increased → timeout in microservice-A.
Severity: HIGH
Fix: Increase DB pool size, enable autoscaling, add request hedging.

⚠ Ticket Created → {'ticket_id': 'INC-7342', 'severity': 'HIGH'}
⏱ Latency: 1.24 seconds
```

## Troubleshooting

| Issue | Fix |
|---|---|
| API key not found | Check `.env` location or environment variable load |
| No logs detected | Ensure files are inside the `logs/` folder |
| Poor analysis | Add more logs → more embeddings → better context |
| ChromaDB error | Delete `vector_store/` folder → rerun |

## Future Enhancements

You can ask the repo maintainer (or me) to generate code for any of these:

| Feature | Prompt to ask |
|---|---|
| LangGraph multi-agent orchestration | "Upgrade to LangGraph Version" |
| Live log streaming analyzer | "Add real-time log ingestion" |
| Dashboard + metrics visualization | "Add observability dashboard" |
| Severity prediction ML model | "Add severity classifier" |
| API integration with Jira/ServiceNow | "Convert fake API → real API" |

---

If you'd like, I can also:

- Convert imports to the modern `langchain` package API and update `requirements.txt`.
- Add a PowerShell script to bootstrap the environment on Windows.
- Create a no-API offline model variant.

Want me to update `requirements.txt` or commit these changes to git? Say the word.
