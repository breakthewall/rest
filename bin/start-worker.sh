#!/bin/bash

app=$1
nb=$2

if [[ "$app" == "" ]]; then
  echo
  echo "Usage:"
  echo
  echo "   `basename $0` <app-name> [nb_of_workers]"
  echo
  exit 1
fi


if [[ "$nb" == "" ]]; then
  nb=1
fi

COMPOSE_PROJECT_NAME=$app docker-compose -f docker-compose-worker.yml up -d --scale worker=$nb
docker network connect $app "$(docker inspect -f '{{.Name}}' $(docker-compose -f docker-compose-flask.yml ps -q)  | cut -c2-)"
