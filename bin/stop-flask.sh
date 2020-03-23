#!/bin/bash
echo docker network disconnect galaxy "$(docker inspect -f '{{.Name}}' $(docker-compose -f docker-compose-flask.yml ps -q)  | cut -c2-)"
docker-compose -f docker-compose-flask.yml down
