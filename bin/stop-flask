#!/bin/bash
docker network disconnect galaxy "$(docker inspect -f '{{.Name}}' $(docker-compose -f docker-compose-flask.yml ps -q)  | cut -c2-)"
REDIS="" docker-compose -f docker-compose-flask.yml down
