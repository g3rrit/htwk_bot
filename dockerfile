FROM alpine

RUN apk add python3 git

ADD . /app

RUN pip3 install -r app/requirements.txt

WORKDIR /app
CMD [ "python3", "main.py", ">>/dev/null", "2>&1"]

