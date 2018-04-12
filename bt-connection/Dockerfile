FROM resin/rpi-raspbian

RUN apt-get update && apt-get install -y \
    bluez \
    redis-tools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR usr/src/app

COPY connect.sh .
COPY bt-pair.sh .

CMD [ "bash", "connect.sh" ]
