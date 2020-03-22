#!/bin/bash


docker run --rm \
  --net flask \
  -v $PWD:/home \
  -w /home \
python:3 bash rest-query.sh
