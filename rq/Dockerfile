ARG IMAGE_NAME

# base image
FROM ${IMAGE_NAME}

# add requirements (to leverage Docker cache)
ADD ./requirements.txt ./requirements.txt

# install requirements
RUN python -m pip install --upgrade pip \
 && python -m pip install -r requirements.txt

#RUN conda install --quiet --yes jsonpickle

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# set working directory
#ARG TOOL_NAME
WORKDIR /home
#/src/app/${TOOL_NAME}
