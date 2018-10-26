#!/bin/bash
docker build -t htwk_bot:latest .
docker run -d htwk_bot:latest
