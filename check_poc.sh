#!/bin/bash
STATUS=""
while [ "$STATUS" != "200" ]
do
    sleep 3
	echo "init is not enough, please wait....."
    STATUS=$(curl -sL -w "%{http_code}" http://127.0.0.1:8000 -o /dev/null)
    
done
sleep 30
poc_result=$(sudo docker-compose logs poc)
echo "$poc_result"

[[ $poc_result =~ "Poc Success!" ]] || exit 1