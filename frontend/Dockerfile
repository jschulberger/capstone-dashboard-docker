FROM node:8.11-alpine
#FROM resin/rpi-raspbian:jessie
EXPOSE 4200

# Add repo, updoot, and install deps
#RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
#RUN apt-get update && apt-get install -y make g++ nodejs
#RUN sudo npm install -g @angular/cli

#Linux setup
RUN apk update \
  && apk add --update alpine-sdk \
  && apk del alpine-sdk \
  && rm -rf /tmp/* /var/cache/apk/* *.tar.gz ~/.npm \
  && npm cache verify \
  && sed -i -e "s/bin\/ash/bin\/sh/" /etc/passwd

# Install js-app deps
RUN npm config set unsafe-perm true
RUN npm install -g @angular/cli@1.6.7

# Create & set app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Move source over
COPY . .
#COPY package*.json ./
#RUN npm install

# Startup command
#CMD [ "npm", "start" ]
