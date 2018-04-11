FROM arm32v7/python:3.6-jessie

RUN apt-get update && apt-get -yq install bluez

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "python", "./obd_sync.py"]
