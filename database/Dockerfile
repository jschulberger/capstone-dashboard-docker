FROM redis:4.0.9-32bit

# Create folder structure
RUN mkdir -p /etc/redis
RUN mkdir -p /var/lib/redis
RUN mkdir -p /var/log/redis
#RUN mkdir -p /var/run/redis

# Copy config file over
COPY redis.conf /etc/redis/redis.conf

CMD [ "redis-server", "/etc/redis/redis.conf" ]
