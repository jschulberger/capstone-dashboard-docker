FROM arm32v7/node:8.11.0
EXPOSE 4200

# Create NPM global directory
RUN mkdir ~/.npm-global
RUN npm config set prefix '~/.npm-global'
RUN touch ~/.profile
RUN echo 'export PATH=~/.npm-global/bin:$PATH' > ~/.profile
RUN source ~/.profile

# Install Angular
RUN npm install -g @angular/cli

# Create app directory
WORKDIR /usr/src/app

# Install app deps
COPY package*.json ./
RUN npm install

# Startup command
CMD [ "npm", "start" ]
