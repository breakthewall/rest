#!/bin/bash

redis=$1

if [[ "$redis" == "" ]]; then
  redis="redis"
fi



REDIS=$redis docker-compose -f docker-compose-flask.yml up -d
docker network connect \
  --alias flask \
  galaxy \
  "$(docker inspect -f '{{.Name}}' $(docker-compose -f docker-compose-flask.yml ps -q)  | cut -c2-)" \
