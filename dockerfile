FROM alpine

RUN apk add python3 git

ADD . /app

RUN pip3 install -r app/requirements.txt

CMD [ "python3", "app/main.py", ">", "app/log/htwk_bot.log", "2>&1"]

