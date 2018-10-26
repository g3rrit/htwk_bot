#!/usr/bin/env sh

sleep 10

FILE_NAME="htwk_bot.pid"

pid="0"
if [ -e "$FILE_NAME" ]; then
    pid=$(cat $FILE_NAME)
fi

# echo $pid

running=$(ps -ef | grep "$pid" | grep -v "grep" | wc -l)
if [ $running -eq 1 ]; then
    echo "program still running"
else
    nohup python3 "main.py" >/dev/null 2>&1 &
fi

nohup "./watchdog.sh" >/dev/null 2>&1 &
