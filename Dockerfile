# maintainer info
FROM alpine:3.18
LABEL maintainer="carrergt@gmail.com"

# copy requirements file
WORKDIR /app
COPY requirements.txt ./

# install python and dependences
RUN apk update
RUN apk add python3 py3-pip
RUN pip3 install -r ./requirements.txt

# copy app
COPY app ./

# start command 
CMD ["sh","./prod.sh"]
EXPOSE 3000
