#!/bin/bash
COMPOSE_PROJECT_NAME=default docker-compose stop flask
docker rm flask
