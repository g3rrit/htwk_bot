#!/bin/bash
docker build -t htwk_bot:latest .
docker run --memory="4g" --cpus="0.5" -d htwk_bot:latest
