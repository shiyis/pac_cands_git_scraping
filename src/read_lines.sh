#!/bin/bash
git clone https://github.com/tweepy/tweepy.git
pwd
cd tweepy
pwd
pip install .
pip install pandas
cd ../
pwd
while read p; do
  delimiter=","
  array=();
  IFS=',' read -r -a array <<< "$p"
  echo ${array[0]}
  echo ${array[3]}
  python ./script/pac_tweet.py --file ./data/${array[0]} --name ${array[3]}
  git config user.name "Automated"
  git config user.email "actions@users.noreply.github.com"
  git add -A
  timestamp=$(date -u)
  git commit -m "Latest data: ${timestamp}" || exit 0
  git push -f origin main
  sleep 20
done <./data/outfile.csv 

