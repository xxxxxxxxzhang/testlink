#!/bin/bash
sleep 600
echo "1111111"
poc_config=`sudo docker-compose logs config`
poc_result=`sudo docker-compose logs poc`
echo "2111111"
echo $poc_config
echo $poc_result

[[ $poc_result =~ "Poc Success!" ]] || exit -1