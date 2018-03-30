FROM node:8

EXPOSE 4200

COPY contents /frontend/
RUN npm install

CMD [ "/usr/local/npm", "start", "--prefix", "/frontend/" ]
