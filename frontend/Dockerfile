FROM node:carbon
EXPOSE 4200

# Create app directory
WORKDIR /usr/src/app

# Install app deps
COPY package*.json ./
RUN npm install

# Bundle app source
COPY . .

# Startup command
CMD [ "npm", "start" ]
