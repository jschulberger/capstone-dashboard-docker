#!/bin/bash

echo "Waiting for front-end..."
echo exit | telnet frontend 4200 &> /dev/null
while [ $? -ne 0 ]; do
    echo exit | telnet frontend 4200 &> /dev/null
done
echo "Front-end is alive"

# Launch wpe display program
/wpe-init &

# Keep checking front-end availability
while [ $? -eq 0 ]; do
    sleep 5s
    echo exit | telnet frontend 4200 &> /dev/null
done

# Front-end must have died, kill display
echo "Front-end has died, killing display..."
exit 1
