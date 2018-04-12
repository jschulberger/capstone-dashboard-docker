#!/bin/bash

if [ -c "/dev/rfcomm0" ]; then
    echo "Connected!"
    sleep 5
    exit 0
fi

OBDII_ADDR="$(redis-cli -s /tmp/redis.sock GET OBDII_ADDR)"

# Check if OBDII is set
if [ ! -z "$OBDII_ADDR" ]; then
    # Get list of available devices
    mapfile -t scanresult < <(hcitool scan)

    # Check if there are any devices available
    if [ ${#scanresult[@]} -le 1 ]; then
        echo "No pairable devices found"
        exit 1
    fi

    # Check if our OBDII ADDR is in the device list
    found=""
    for (( i=1; i<${#scanresult[@]}; i++ )); do
        if [[ ${scanresult[i]} =~ $OBDII_ADDR ]]; then
            found="true"
        fi
    done

    if [ "$found" == "true" ]; then
        bash bt-pair.sh "$OBDII_ADDR" | bluetoothctl
        rfcomm bind rfcomm0 "$OBDII_ADDR"
        exit 0
    else
        echo "Specific device not found"
        exit 1
    fi
else
    echo "No OBDII address set"
    exit 1
fi

exit 0
