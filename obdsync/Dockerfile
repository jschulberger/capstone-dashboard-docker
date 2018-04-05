FROM arm32v7/python:3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "python", "./obd_sync.py"]
