FROM openjdk:17-slim

RUN apt-get update && apt-get install -y python3 python3-pip wget

RUN wget https://github.com/AsamK/signal-cli/releases/download/v0.13.4/signal-cli-0.13.4.tar.gz \
    && tar -xzf signal-cli-0.13.4.tar.gz \
    && mv signal-cli-0.13.4/bin/signal-cli /usr/local/bin/ \
    && mv signal-cli-0.13.4/lib /usr/local/lib/signal-cli

WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY bot.py .

CMD ["python3", "bot.py"]
