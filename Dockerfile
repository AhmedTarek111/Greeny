# start docker with python 3.11
FROM python:3.11.6-slim-bullseye

# SETUP LINUX PYTHON 
ENV PYTHONUNBUFFERED = 1

# UPDATE LINUX KERNAL & SETUP TOOLS 

RUN apt-get update && \apt-get -y install gcc libpq-dev
# make folder for 
WORKDIR /app


# copy & install 
COPY requirements.txt /app/requirements.txt

# install requirements 
RUN pip install -r /app/requirements.txt

# copy project folder 
COPY . /app/
