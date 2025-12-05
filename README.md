# Incident Tracking AI Agent

Lightweight incident-tracking AI assistant project.

Overview

This repository contains a minimal agent for tracking and summarizing incidents. The project is prepared for containerized deployment and CI/CD to Render via GitHub Actions.

Quick start (local)

1. Create and activate a virtual environment (PowerShell):

```
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Install dependencies and run:

```
pip install -r requirements.txt
python main.py
```

Docker (build & run)

```
docker build -t incident-tracking-ai-agent:latest .
docker run -p 8000:8000 --env-file .env incident-tracking-ai-agent:latest
```

CI / Deploy to Render (GitHub Actions)

This repo includes a GitHub Actions workflow at `.github/workflows/render-deploy.yml` that builds and pushes a Docker image and triggers a Render deploy.

Required GitHub Secrets

- `DOCKERHUB_USERNAME` – Docker Hub username
- `DOCKERHUB_TOKEN` – Docker Hub access token
- `RENDER_SERVICE_ID` – Render service id to deploy
- `RENDER_API_KEY` – Render API key with deploy permissions

Notes

- The Dockerfile uses `python main.py` as the default command. If your app is ASGI/uvicorn-based, change the Dockerfile `CMD` to use `uvicorn main:app --host 0.0.0.0 --port $PORT` or your preferred production server.
- A corrected `requirements.txt` was added (the repo also contains the original `requirenments.txt`).
