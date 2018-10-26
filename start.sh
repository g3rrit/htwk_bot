#!/bin/sh

nohup python3 main.py >/dev/null 2>&1 &
sleep 5
nohup ./watchdog.sh >/dev/null 2>&1 &
tail -f /dev/null
