FROM python:3.5-alpine

WORKDIR /usr/src

RUN apk update && \
    apk add mariadb-dev python-dev

ADD requirements.txt /usr/src

RUN pip install -r requirements.txt


