FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
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

# Install Node.js + npm (required for Robot Framework Browser)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && \
    pip install \
        robotframework \
        robotframework-browser \
        robotframework-retryfailed \
        robotframework-pythonlibcore \
        requests \
        tox

# Install Playwright browsers
RUN rfbrowser init --with-deps

WORKDIR /home/jenkins/agent/workspace/Basic-SWT-Pipeline

CMD ["bash"]
