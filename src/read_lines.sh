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
  echo ${array[1]}
  python ./script/pac_tweet.py --out_file data/${array[1]} --cand_name ${array[3]}
  sleep 5
done <./data/outfile.csv 

