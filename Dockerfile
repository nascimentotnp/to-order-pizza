FROM python:3

WORKDIR /home/worker/src/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT --log-level warning" ]
