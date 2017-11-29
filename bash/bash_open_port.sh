# Usage: ./bash_open_port.sh 9042
#!/usr/bin/env bash

# mac
p=`lsof -i :${1}`

if [ ! -z "$p" ];
then
    echo "Port ${1} is open!"
fi
