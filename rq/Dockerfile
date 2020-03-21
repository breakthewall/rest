ARG IMAGE

# base image
FROM ${IMAGE}

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements (to leverage Docker cache)
ADD ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

#RUN conda install --quiet --yes jsonpickle

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
