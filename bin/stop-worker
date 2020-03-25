#!/bin/bash
app=$1


if [[ "$app" == "" ]]; then
  echo
  echo "Usage:"
  echo "   `basename $0` <app-name>"
  echo
  exit 1
fi

docker network disconnect $app "$(docker inspect -f '{{.Name}}' $(docker-compose -f docker-compose-flask.yml ps -q)  | cut -c2-)"
COMPOSE_PROJECT_NAME=$app docker-compose -f docker-compose-worker.yml down
