FROM nginx:mainline-alpine

RUN apk add --no-cache --progress python3 openssl
RUN pip3 --no-cache-dir install flask
RUN wget -O /usr/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-init_1.2.1_amd64
RUN chmod +x /usr/bin/dumb-init

ADD . /firehose
RUN pip3 install -e /firehose
RUN cp -r /firehose/testapp /app
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
	-keyout /app/nginx-selfsigned.key \
	-out /app/nginx-selfsigned.crt \
	-subj "/C=GB/ST=London/L=London/O=Global Security/OU=IT Department/CN=localhost"
RUN chmod +x /app/exec.sh

EXPOSE 443
WORKDIR /app
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["/app/exec.sh"]
