FROM resin/rpi-raspbian:jessie
EXPOSE 4200

# Add repo, updoot, and install deps
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get update && apt-get install -y \
    make \
    g++ \
    nodejs \
    && rm -rf /var/lib/apt/lists/*

# Install js-app deps
RUN npm config set unsafe-perm true
RUN npm install -g @angular/cli

# Create & set app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Move source over
COPY c43539a/. .

# Set connection vars
RUN sed -i 's,^\(var refreshInterval = \).*,\135;,' /usr/src/app/server.js
RUN sed -i 's,^\(var client = redis.createClient(\).*,\1"/tmp/redis.sock");,' /usr/src/app/server.js
RUN sed -i 's,^\(const myURL = \).*,\1"http://frontend:4200",' /usr/src/app/src/app/app.module.ts

# Install the app
RUN npm install

# Build final files
RUN ng build

# Startup command
CMD [ "node", "server" ]
