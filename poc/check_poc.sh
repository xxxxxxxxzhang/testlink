#!/bin/bash
sleep 200
config_result=`sudo docker-compose logs poc`

echo $config_result

[[ $config_result =~ "Poc Success!" ]] || exit -1