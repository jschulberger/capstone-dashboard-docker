FROM arm32v7/python:3.6.5-slim-stretch

RUN apt-get update && apt-get install -y \
    bluez \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "python", "./obd_sync.py"]
