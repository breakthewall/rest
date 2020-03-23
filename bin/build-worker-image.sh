#!/bin/bash

app=$1
from_image=$2

if [[ "$app" == "" ]]; then
  echo
  echo "Usage:"
  echo
  echo "   `basename $0` <app-name> [nb_of_workers]"
  echo
  exit 1
fi

if [[ "$from_image" == "" ]]; then
  from_image=$app
fi

COMPOSE_PROJECT_NAME=$app IMAGE=$from_image docker-compose build worker
