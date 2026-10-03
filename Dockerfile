FROM eclipse-temurin:21-jre

RUN apt-get update \
    && apt-get install -y python3 python3-pip wget ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/AsamK/signal-cli/releases/download/v0.14.8/signal-cli-0.14.8.tar.gz \
    && tar -xzf signal-cli-0.14.8.tar.gz \
    && mv signal-cli-0.14.8 /opt/signal-cli \
    && ln -s /opt/signal-cli/bin/signal-cli /usr/local/bin/signal-cli \
    && rm signal-cli-0.14.8.tar.gz

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

COPY bot.py .

CMD ["python3", "bot.py"]
