FROM arm32v7/redis:4

# Create folder structure
#UN mkdir -p /etc/redis
RUN mkdir -p /var/lib/redis
#RUN mkdir -p /var/log/redis
#RUN mkdir -p /var/run/redis

# Copy config file over
COPY redis.conf /usr/local/etc/redis/redis.conf

# Set permissions
#RUN chmod 777 -R /etc/redis
RUN chmod 777 -R /var/lib/redis
#RUN chmod 777 /var/log/redis_sock.log
#RUN chmod 777 -R /var/run/redis

CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]
