#FROM arm32v7/node:carbon
FROM resin/rpi-raspbian:jessie
EXPOSE 4200

SHELL ["/bin/bash", "-c"]

# Add repo, updoot, and install deps
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get update && apt-get install -y make g++ nodejs
#RUN sudo npm install -g @angular/cli

# Create & set app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install js-app deps
ARG NPM_CONFIG_PREFIX=~/.npm-global
RUN source ~/.profile && npm install @angular/cli
#source ~/.profile
#npm install -g @angular/cli

COPY . .
#COPY package*.json ./
#RUN npm install

# Startup command
#CMD [ "npm", "start" ]
