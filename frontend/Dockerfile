#FROM arm32v7/node:carbon
FROM resin/rpi-raspbian:jessie
EXPOSE 4200

# Add repo, updoot, and install deps
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get update && apt-get install -y git make g++ nodejs
#RUN sudo npm install -g @angular/cli

RUN mkdir -p /usr/src/app

# Create app directory
WORKDIR /usr/src/app

# Install app deps
COPY . .
#COPY package*.json ./
#RUN npm install

# Startup command
#CMD [ "npm", "start" ]
