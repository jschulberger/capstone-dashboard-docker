#!/bin/bash
telnet frontend 4200
while [ $? -ne 0 ]; do
  telnet frontend 4200
done

/wpe-init
