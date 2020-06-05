#!/bin/bash
tar -xvzf /opt/data/geckodriver-v0.26.0-linux64.tar.gz 
chmod +x geckodriver 
cp geckodriver /usr/local/bin/ 
STATUS=""
while [ "$STATUS" != "200" ]
do
    sleep 1
    STATUS=$(curl -sL -w "%{http_code}" http://web -o /dev/null)
done
python3 opt/data/filldata.py http://web 
echo "config ok"