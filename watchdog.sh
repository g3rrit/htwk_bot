#!/usr/bin/env sh

sleep 10
pid = $(cat htwk_bot.pid)
if $(pidof python3 | grep $pid); then
    echo "program still running"
else
    nohup python3 main.py >>/dev/null 2>&1 &
fi
nohup sh -c watchdog.sh &