# Usage: ./bash_detect_docker_machine.sh

#!/usr/bin/env bash

# default docker machine name to check
DOCKER_MACHINE_NAME="default"

# check if the docker machine exists
if [[ $(docker-machine ls -q | grep "^${DOCKER_MACHINE_NAME}$") = $DOCKER_MACHINE_NAME ]];
then
    echo "Found"

    # get the ip of the docker machine
    DOCKER_MACHINE_IP="$(docker-machine ip $DOCKER_MACHINE_NAME)"

    # check if we got the ip
    if [ -z "${DOCKER_MACHINE_IP}" ];
    then
        # the docker machine is not up
        echo "Docker machine is down"
    else
        # print the docker machine ip
        echo $DOCKER_MACHINE_IP
    fi

else
    # no docker machine registered with the name specified in DOCKER_MACHINE_NAME
    echo "Not Found"
fi
