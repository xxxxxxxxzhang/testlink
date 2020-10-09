#!/bin/bash
STATUS=""
while [ "$STATUS" != "200" ]
do
    sleep 3
	echo "init is not enough, please wait....."
    STATUS=$(curl -sL -w "%{http_code}" http://127.0.0.1:8000 -o /dev/null)
    
done
sleep 20
config_result=$(sudo docker-compose logs config)

echo "$config_result"

[[ $config_result =~ "Config Success!" ]] || exit 1