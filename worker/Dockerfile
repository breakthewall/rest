ARG BASE_IMAGE_NAME

FROM ${BASE_IMAGE_NAME}

WORKDIR /home

ARG TOOL_DIR
COPY ${TOOL_DIR}/worker.py .

# add requirements (to leverage Docker cache)
ADD worker/requirements.txt ./requirements.txt

# install requirements
RUN python -m pip install --upgrade pip \
 && python -m pip install -r requirements.txt

#RUN conda install --quiet --yes jsonpickle

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

ARG PROJECT_NAME
# Make consistent with flask import paths in @app.route
RUN mkdir -p tools \
 && ln -sf $PWD tools/${PROJECT_NAME}

COPY worker/request.py .
