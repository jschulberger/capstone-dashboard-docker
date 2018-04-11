#!/bin/bash

# Wait until frontend is ready
echo "[display] Waiting for frontend..."
echo exit | telnet frontend 4200 &> /dev/null
while [ $? -ne 0 ]; do
  echo exit | telnet frontend 4200 &> /dev/null
done
echo "[display] Frontend is alive!"

# Start main script
/wpe-init
