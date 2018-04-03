#!/bin/bash
echo exit | telnet frontend 4200 &> /dev/null
while [ $? -ne 0 ]; do
  echo exit | telnet frontend 4200 &> /dev/null
done

/wpe-init
