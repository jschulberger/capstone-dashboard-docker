FROM arm32v7/node:carbon
EXPOSE 4200

# Create app directory
WORKDIR /usr/src/app

# Install app deps
COPY package*.json ./
RUN npm install

# Startup command
CMD [ "npm", "start" ]
