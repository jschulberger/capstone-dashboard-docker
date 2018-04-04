FROM arm32v7/redis:4

# Allow DB saving
RUN chmod 777 /usr/local/lib

# Copy config file over
COPY redis.conf /usr/local/etc/redis/redis.conf

CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]
