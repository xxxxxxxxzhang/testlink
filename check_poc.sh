#!/bin/bash
sleep 600
poc_result=`sudo docker-compose logs poc`
echo $poc_result

[[ $poc_result =~ "Poc Success!" ]] || exit 1