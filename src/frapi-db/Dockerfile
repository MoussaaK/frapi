#Using alpine 3.7
FROM alpine:3.7

#Install MongoDB
RUN apk update
RUN apk add --no-cache mongodb mongodb-tools
RUN mkdir -p /data/db && chown -R mongodb:mongodb /data/db

WORKDIR /code

COPY . /code

VOLUME ["/data/db"]

EXPOSE 27017 28017

CMD ["mongod", "--bind_ip", "0.0.0.0"]
