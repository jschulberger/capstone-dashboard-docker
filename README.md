# Capstone Dashboard Docker
A collection of containers that are designed to be deployed via Resin.IO to remote devices. Each container is a dependency that the front-end requires to gather data from a vehicle.

# How to Deploy


# About the project


# Container Descriptions
bt-connection
* Retrieves a MAC address from Redis of the Bluetooth device that should be paired. A connection is then created and maintained (in the case of a disconnect) throughout the execution of the script.

database
* Hosts a Redis server that is accessible via a unix socket. This socket can be shared with other containers and is, by default, at /tmp/redis.sock.

display
* Accesses the node server hosted within the front-end container. More information on the base image for WPE-WebKit can be found at https://github.com/resin-io-projects/resin-wpe.

front-end
* Hosts the compiled angular front-end files with minimal node dependencies installed. Compilation occurs via deployment with source files gathered from https://github.com/matthewfortier/Capstone-Dashboard.

obdsync
* Pulls requested OBD-II PIDs from Redis, retrieves the corresponding data from the vehicle, and sends the response back to Redis.
