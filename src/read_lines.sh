#!/bin/bash
# git clone https://github.com/tweepy/tweepy.git
# pwd
# cd tweepy
# pwd
# pip install .
pip install tweepy
pip install pandas
# cd ../
# pwd
python ./script/pac_tweet.py


# while read p; do
#   delimiter=","
#   array=();
#   IFS=',' read -r -a array <<< "$p"
#   echo ${array[0]}
#   echo ${array[3]}
#   python ./script/pac_tweet.py --file ./data/${array[0]} --name ${array[3]}
#   sleep 5
# done <./data/outfile.csv 

