FROM ubuntu:latest
LABEL authors="laikov"

ARG BRANCH_NAME=""

WORKDIR /shell-mvp-tests

COPY requirements.txt /
COPY shell-mvp-tests .

RUN apt-get update && apt-get install -y python3 python3-venv python3-pip

RUN python3 -m venv venv

RUN . venv/bin/activate

RUN pip install -r requirements.txt
RUN mkdir /report
