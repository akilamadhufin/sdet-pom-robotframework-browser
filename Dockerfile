FROM python:3.10-slim

# System dependencies for Playwright
RUN apt-get update && apt-get install -y \
    wget \
    xvfb \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libxshmfence1 \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies
RUN pip install --upgrade pip && \
    pip install \
        robotframework \
        robotframework-browser \
        robotframework-retryfailed \
        robotframework-pythonlibcore \
        requests \
        tox

# Install Playwright browsers for Robot Framework Browser
RUN rfbrowser init

# Workspace inside container
WORKDIR /workspace

# Default command
CMD ["bash"]
