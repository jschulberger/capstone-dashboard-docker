FROM arm32v7/redis:4

# Create folder structure
RUN mkdir -p /etc/redis
RUN mkdir -p /var/lib/redis
#RUN mkdir -p /var/log/redis
#RUN mkdir -p /var/run/redis

# Copy config file over
COPY redis.conf /etc/redis/redis.conf
RUN touch /var/log/redis_sock.log

# Set permissions
RUN chmod 777 -R /etc/redis
RUN chmod 777 -R /var/lib/redis
#RUN chmod 777 -R /var/log/redis
#RUN chmod 777 -R /var/run/redis

CMD [ "redis-server", "/etc/redis/redis.conf" ]
