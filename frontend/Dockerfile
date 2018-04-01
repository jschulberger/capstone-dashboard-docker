#FROM arm32v7/node:carbon
FROM resin/rpi-raspbian:jessie
EXPOSE 4200

RUN apt-get update && apt-get install -y git make g++

RUN curl -sL https://deb.nodesource.com/setup_$MAJ_VERSION.x | bash -
RUN apt-get install -y nodejs
RUN sudo npm install -g @angular/cli

RUN mkdir -p /usr/src/app

# Create app directory
WORKDIR /usr/src/app

# Install app deps
COPY . .
#COPY package*.json ./
#RUN npm install

# Startup command
#CMD [ "npm", "start" ]
