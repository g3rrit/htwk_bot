#!/bin/bash

# you probably need to call this with 'id_rsa=$(~/.ssh/id_rsa);sudo ./create_docker.sh "$id_rsa"' to be able to use !restart command

docker build -t htwk_bot:latest --build-arg id_rsa_key="$1" .
docker run --memory="4g" --cpus="0.5" -d htwk_bot:latest
