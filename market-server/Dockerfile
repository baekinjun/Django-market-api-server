# Base Image
FROM ubuntu:18.04
FROM python:3.6.8-stretch

ENV PYTHONUNBUFFERED 1

# General Packages
RUN apt-get update \
    && apt-get install -y software-properties-common \
    && apt-get install -y build-essential \
    && apt-get install -y python-dev \
    && apt-get install -y python-pip \
    && apt-get install -y python3-pip \
    && apt-get update \
    && apt-get install -y default-libmysqlclient-dev \
    && apt-get install -y git

# Setup Cron
RUN apt-get update && apt-get -y install cron
RUN touch /var/log/cron.log
CMD cron && tail -f /var/log/cron.log

# Set locale
ENV LC_ALL=C.UTF-8

# Upgrading pip
RUN python -m pip install pip --upgrade
RUN apt-get update

# Setup Folders
RUN mkdir -p /market-server

# Move to working directory
WORKDIR /market-server

# Add working directory
COPY . /market-server

# Setup requirements
RUN cd /market-server \
    && pip3 install -r requirements.txt

# Open Port for the Python App
EXPOSE 1310