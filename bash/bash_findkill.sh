# Usage: ./bash_findkill.sh <servicename>

#!/bin/bash

# -- NICE: try to use killall to stop process(s)
killall ${1} > /dev/null 2>&1 ;sleep 10

# -- if we do not see the process, just end the function
pgrep ${1} > /dev/null 2>&1 || return

# -- UGLY: Step trough every pid and use kill -9 on them individually
for PID in $(pidof ${1}) ;do

    echo "Terminating Process: [${1}], PID [${PID}]"
    kill -9 ${PID} ;sleep 10

    # -- NASTY: If kill -9 fails, try SIGTERM on PID
    if ps -p ${PID} > /dev/null ;then
        echo "${PID} is still running, forcefully terminating with SIGTERM"
        kill -SIGTERM ${PID}  ;sleep 10
    fi

done

# -- If after all that, we still see the process, report that to the screen.
pgrep ${1} > /dev/null 2>&1 && echo "Error, unable to terminate all or any of [${1}]" || echo "Terminate process [${1}] : SUCCESSFUL"