#!/bin/bash

docker stop $(docker ps -a -q  --filter ancestor=htwk_bot:latest)
docker system prune -a -f --filter "label=htwk_bot:latest"
