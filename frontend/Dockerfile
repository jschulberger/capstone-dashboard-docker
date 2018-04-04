FROM resin/rpi-raspbian:jessie
EXPOSE 4200

# Add repo, updoot, and install deps
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get update && apt-get install -y make g++ nodejs

# Install js-app deps
RUN npm config set unsafe-perm true
RUN npm install -g @angular/cli

# Create & set app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Move source over
COPY . .

# Move package only
#COPY package*.json ./

# Set connection vars
RUN sed -i 's,^\(var refreshInterval = \).*,\1'80',' /usr/src/app/server.js
RUN sed -i 's,^\(\tclient = redis.createClient(\).*,\1"/tmp/redis.sock");,' /usr/src/app/server.js
RUN sed -i 's,^\(const myURL = \).*,\1"http://frontend:4200",' /usr/src/app/src/app/app.module.ts

# Install the app
RUN npm install

# Startup command
CMD [ "npm", "start" ]
