FROM alpine

RUN apk add python3 git openssh-client

ADD . /app
ADD ~/.ssh/id_rsa.pub /root/.ssh/id_rsa.pub

RUN pip3 install -r app/requirements.txt

WORKDIR /app
RUN watchdog.sh
CMD [ "python3", "main.py", ">>/dev/null", "2>&1"]

