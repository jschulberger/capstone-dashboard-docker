FROM arm32v7/redis:4

# Create folder structure
RUN mkdir -p /etc/redis
RUN mkdir -p /var/lib/redis
RUN mkdir -p /var/log/redis
#RUN mkdir -p /var/run/redis

# Copy config file over
COPY redis.conf /etc/redis/redis.conf

# Set permission
RUN chmod 777 -R /etc/redis
RUN chmod 777 -R /var/lib/redis
RUN chmod 777 -R /var/log/redis


CMD [ "redis-server", "/etc/redis/redis.conf" ]
