###################
# Build Container #
###################
FROM resin/rpi-raspbian:jessie as builder

# Add repo, updoot, and install deps
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get update && apt-get install -yq \
    make \
    g++ \
    git \
    nodejs \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Install js-app deps
RUN npm config set unsafe-perm true
RUN npm install -g @angular/cli

# Create & set app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Allow forcing rebuild
ARG CACHEBUST=3

# Retrieve source
RUN git clone https://github.com/matthewfortier/Capstone-Dashboard .

# Set connection vars
RUN sed -i 's,^\(var refreshInterval = \).*,\170;,' /usr/src/app/server.js
RUN sed -i 's,^\(var client = redis.createClient(\).*,\1"/tmp/redis.sock");,' /usr/src/app/server.js
RUN sed -i 's,^\(const myURL = \).*,\1"http://frontend:4200";,' /usr/src/app/src/app/app.module.ts

# Install the app
RUN npm install

# Build final files
RUN ng build

###################
# Final container #
###################
FROM resin/rpi-raspbian:jessie
EXPOSE 4200

# Add repo, updoot, and install deps
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get update && apt-get install -yq \
    nodejs \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Create & set app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install project dependencies
RUN npm install \
    body-parser \
    express \
    http \
    path \
    redis \
    socket.io

# Move compiled source
COPY --from=builder /usr/src/app/dist dist
COPY --from=builder /usr/src/app/re-direct-page.html re-direct-page.html
COPY --from=builder /usr/src/app/server.js server.js

# Startup command
CMD [ "node", "server" ]
