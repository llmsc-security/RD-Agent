# Multi-stage build for RD-Agent
# Stage 1: Build stage
FROM python:3.11-slim AS builder

WORKDIR /build

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Runtime stage
FROM python:3.11-slim

# Create non-root user
RUN groupadd -g 1000 rdagent && \
    useradd -u 1000 -g rdagent -m rdagent -d /home/rdagent

WORKDIR /home/rdagent

# Copy installed packages from builder
COPY --from=builder /root/.local /home/rdagent/.local

# Ensure scripts in .local are usable
ENV PATH=/home/rdagent/.local/bin:$PATH

# Copy the application code
COPY rdagent/ ./rdagent/
COPY pyproject.toml ./pyproject.toml
COPY README.md ./README.md

# Create log directory with proper permissions
RUN mkdir -p /home/rdagent/log && \
    mkdir -p /home/rdagent/.local/share && \
    chown -R rdagent:rdagent /home/rdagent

# Switch to non-root user
USER rdagent

# Expose Flask server port
EXPOSE 19899

# Default command starts the Flask server
CMD ["python", "-m", "rdagent.log.server.app", "--port=19899", "--host=0.0.0.0"]
