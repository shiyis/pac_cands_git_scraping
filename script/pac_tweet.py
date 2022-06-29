import tweepy
import pandas as pd
import time
import random
import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('--name', help='cand name')
# parser.add_argument('--file', help='output file')
# args = parser.parse_args()

consumer_key = "YOUR KEY"
consumer_secret = "YOUR KEY"
bearer_token = "YOUR KEY"
access_token = "YOUR KEY"
access_token_secret = "YOUR KEY"

# Replace with your own search query

client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    wait_on_rate_limit=True,
)


cands = pd.read_csv("./input/outfile_6.csv")

for n, row in cands.iterrows():
    try:
        response = client.get_user(username=row["id"])
        id = response.data.id

        tweets = client.get_users_tweets(
            id=id,
            tweet_fields=["context_annotations", "id", "created_at", "geo", "text",],
            max_results=100,
        )

        # Pulling information from tweets iterable object and adding relevant tweet information in our data frame
        user_tweets = []
        for tweet in tweets.data:
            user_tweets.append(
                {
                    "Created at": tweet.created_at,
                    "User ID": tweet.id,
                    "Text": tweet.text,
                }
            )
        df_user_tweets = pd.DataFrame(user_tweets)
        print(df_user_tweets)
        df_user_tweets.to_csv("./data/" + row["filename"])
        time.sleep(20)
    except:
        pass
