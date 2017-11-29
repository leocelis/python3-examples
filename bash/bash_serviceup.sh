#!/usr/bin/env bash

while [[ $(nc 127.0.0.1 9042 < /dev/null; echo $?) = 1 ]]
do
    echo "Not running"
    sleep 1
done

echo "It's running!"
