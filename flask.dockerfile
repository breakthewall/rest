# base image
FROM python:3.8.0-alpine

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements (to leverage Docker cache)
ADD ./requirements-flask.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# # copy project
# COPY . /usr/src/app

EXPOSE 8000
