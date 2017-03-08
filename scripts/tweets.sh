#!/bin/sh
touch rawData.txt
echo "starting stream">log.txt
nodejs ../Node1/bot.js> rawData.txt #stream tweets
echo "finished stream">log.txt
python jsonToCassandra.py rawData.txt #store tweets in Cassandra DB
rm rawData.txt
echo "running analysis">log.txt
python tweetsToStates.py
echo "getting averages">log.txt
python DB_to_UI.py
