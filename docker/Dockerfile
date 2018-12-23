# -*- mode: dockerfile -*-

FROM ubuntu:17.10

MAINTAINER Andrii Tkachenko "tas.gma@gmail.com"

USER root

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
	   build-essential \
	   procps \
	   net-tools \
	   wget \
	   git \
	   python3-pip \
	   python3-wheel \
	   python3 \
	   python3-dev \
	   python3-setuptools \
	   iputils-ping \
	   libmysqlclient-dev \
	   tzdata \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY --from=node:8.11.3 /usr/local/lib/node_modules/npm /usr/local/lib/node_modules/npm/
COPY --from=node:8.11.3 /usr/local/bin/ /usr/local/bin/

WORKDIR /opt/quiz

EXPOSE 8283

ADD ./requirements.txt /

RUN pip3 install -r /requirements.txt

ENV SETTINGS="settings.base" \
	TZ="Europe/Kiev"

CMD ./run.py --settings="${SETTINGS}"
