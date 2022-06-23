import tweepy
from tweepy import OAuthHandler
import pandas as pd
import time


consumer_key = "8mpjTaSxQRTKDqA49l4EUo5Hi"
consumer_secret = "MjqTyxSBDNSw6glSSxIZFlc8ye1eDX39pt8NVSqwJpaq82AdRw"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAGwReAEAAAAAMfSyoixFQyWmofzkvQzS8dBHK%2Fs%3D6hXcF5Nhdn35zIs1bsGwe7DErFcFhl6GK9RdpHXjK1Ry2YuWxt"
access_token = '1460714174754037761-ChtNeYlhVtwbwUhNze32Zd1VkqQsR0'
access_token_secret = 'RR1ujY0vEuBJVqBJ8tFh5uNLqrmqZAwuxs9zsjdJ3E3BW'

# Replace with your own search query

client = tweepy.Client( bearer_token=bearer_token, 
                        consumer_key=consumer_key, 
                        consumer_secret=consumer_secret, 
                        access_token=access_token, 
                        access_token_secret=access_token_secret, 
                        wait_on_rate_limit=True)

cands = pd.read_csv('data/outfile.csv')
for n , row in cands.iterrows():

  response = client.get_user(username=row['id'])
  id = response.data.id
  tweets = client.get_users_tweets(id=id, tweet_fields=['context_annotations','id','created_at','geo',"text",],max_results=100)


  df_user_tweets = pd.DataFrame()

  # Pulling information from tweets iterable object and adding relevant tweet information in our data frame
  for tweet in tweets.data:
    df_user_tweets = df_user_tweets.append(
      {'Created at': tweet.created_at,
        'User ID': tweet.id,
        'Text': tweet.text,
        }, ignore_index=True)
  df_user_tweets.to_csv('data/' + row['filename'])
