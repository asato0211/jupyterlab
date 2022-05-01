FROM python:3-slim

RUN apt-get update && apt-get install -y \
  default-libmysqlclient-dev \
  build-essential \
  pkg-config

WORKDIR /lab

COPY requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip \
  && python3 -m pip install -r requirements.txt
