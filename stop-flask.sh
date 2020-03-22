#!/bin/bash
COMPOSE_PROJECT_NAME=default-app docker-compose stop flask
docker rm flask
