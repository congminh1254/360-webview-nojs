# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install waitress

COPY . .

CMD [ "python3", "waitress_server.py" ]