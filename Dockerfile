FROM python:3.13.9-slim

WORKDIR /app

# install minimal system deps required for building some Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment inside the image (per request)
ENV VENV_PATH=/opt/venv
RUN python -m venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

# copy requirements and install into the venv
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# copy app sources
COPY . /app

ENV PORT=8000
EXPOSE 8000

# Default command: change to uvicorn if using FastAPI app
CMD ["python", "main.py"]
