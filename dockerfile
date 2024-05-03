# syntax=docker/dockerfile:1



FROM python:latest

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /work/app

RUN python -m venv venv

ENV PATH="/work/app/venv//bin:$PATH"

# Copy the source code into the container.
COPY . .


RUN pip install --no-cache-dir -r requirements.txt
# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD ["venv/bin/python", "./script.py"]


