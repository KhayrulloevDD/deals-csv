# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /django
COPY requirements.txt /django/
RUN pip install -r requirements.txt
COPY . /django