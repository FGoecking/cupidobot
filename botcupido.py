from os import read, write
import tweepy
import time
import random

api_key = ''
api_secret_key = ''

access_token = ''
secret_access_token = ''

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, secret_access_token)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search = '#Solteira'
numeroDeTweets = 10

for tweet in tweepy.Cursor(api.search, search).items(numeroDeTweets):
    try:
        print('tweet retuitado')
        tweet.retweet()
        time.sleep(60)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break