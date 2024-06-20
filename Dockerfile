FROM python:3

LABEL mainteiner=luizlagj

ENV PORT=$app_port

# Install necessary packages
RUN pip install uvicorn==0.23.2

# Use the same base image for runtime
FROM python:3.10.10-alpine3.17 as runtime

RUN adduser -D worker

USER worker

WORKDIR /home/worker

ENV PATH="/home/worker/.local/bin:${PATH}"

# Copy dependencies from the build stage
COPY --from=build /usr/local/ /usr/local

# Copy application files
COPY requirements.txt /tmp/requirements.txt
COPY app/ /home/worker/src/

# Install dependencies for the application
RUN pip install --user -r /tmp/requirements.txt

# Set permissions and finalize the setup
COPY --chown=worker:worker . .

# Make sure you are in the correct working directory
WORKDIR /home/worker/src/

# Ensure you point to the correct script
CMD [ "sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT --log-level warning" ]