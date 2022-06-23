#!/bin/bash
git clone https://github.com/tweepy/tweepy.git
pwd
cd tweepy
pwd
pip install .
pip install pandas
python ./script/pac_tweet.py
# while read p; do
#   delimiter=","
#   array=();
#   IFS=',' read -r -a array <<< "$p"
#   echo ${array[1]}
#   facebook-scraper -c src/cookies.json -p 100 --filename data/${array[1]} ${array[3]}
# done <data/outfile.csv
