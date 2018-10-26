#!/bin/bash

docker stop $(docker ps -a -q  --filter ancestor=htwk_bot:latest)
