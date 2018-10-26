FROM alpine

ARG id_rsa_key
RUN apk add openssh-client python3 git

ADD . /app
RUN mkdir /root/.ssh
RUN echo "$id_rsa_key" > /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa

RUN pip3 install -r app/requirements.txt

WORKDIR /app

CMD [ "./start.sh" ]

