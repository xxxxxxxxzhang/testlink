#!/bin/bash
sleep 300
echo "1111111"
poc_result=`sudo docker-compose logs poc`
echo "2111111"
echo $poc_result

[[ $poc_result =~ "Poc Success!" ]] || exit -1