#!/bin/bash
app=$1


if [[ "$app" == "" ]]; then
  echo
  echo "Usage:"
  echo "   `basename $0` <app-name>"
  echo
  exit 1
fi

COMPOSE_PROJECT_NAME=$app docker-compose stop worker
docker network disconnect $app flask
