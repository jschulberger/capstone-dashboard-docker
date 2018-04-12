#!/bin/bash
echo -e 'power on\n'
sleep 1
echo -e 'scan on\n'
sleep 5
echo -e 'agent on\n'
sleep 1
echo -e 'default-agent\n'
sleep 1
echo -e "pair $1\n"
sleep 2
echo -e "1234\n"
sleep 1
echo -e 'quit\n'
