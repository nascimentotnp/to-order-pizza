FROM python:3.10.10-alpine3.17 as build

LABEL mainteiner=luizlagj

ENV PORT=$app_port 

#RUN pip install debugpy
RUN pip install uvicorn==0.23.2


FROM python:3.10.10-alpine3.17 as runtime

RUN adduser -D worker

USER worker

WORKDIR /home/worker

ENV PATH="/home/worker/.local/bin:${PATH}"

COPY --from=build /usr/local/ /usr/local
COPY requirements.txt /tmp/requirements.txt
COPY app/ /home/worker/src/

RUN pip install --user -r /tmp/requirements.txt

COPY --chown=worker:worker . .
WORKDIR /home/worker/src/
CMD [ "sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT --log-level warning" ]