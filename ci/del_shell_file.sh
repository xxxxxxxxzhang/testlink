#!/bin/bash

IF_DELETE_INSTALL_FILE=1
WEBSHELL_FILE="/opt/bitnami/testlink/logs/shell.php"

if [ ${IF_DELETE_INSTALL_FILE} == 1 ];
then
    sudo docker exec -it web-app /bin/sh -c 'rm '${WEBSHELL_FILE}
    echo "Delete finished!"

fi