#FROM node:8.11-alpine
FROM jschulberger/resin-wpe

COPY startup.sh .
RUN chmod +x startup.sh

# Startup command
CMD [ "/startup.sh" ]
