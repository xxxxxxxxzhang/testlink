#!/bin/bash
sleep 300
config_result=`sudo docker-compose logs poc`


[[ $config_result =~ "Poc Success!" ]] || exit -1