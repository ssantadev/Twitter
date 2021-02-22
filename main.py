# -*- coding: utf-8 -*-
import sys
import tweepy
import json

# Autenticações
consumer_key = "4C01PjIV6cXsmGw6p6N0SoRuE"
consumer_secret = "KNiyMxTrtzwxDRljlqNfJTZIOqAbCgTq1jdNvWk86BKvxVv2vY"
access_token = "917511810688999424-wuhA3qMtQ0aqywjcNKvbfc6IU4i65VD"
access_token_secret = "OuwBWadPlNFw5XbRfZFDGcIFygi6DzumtAkf4rEpFjmKx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
trendingtweet = api.trends_place(1)

# Where On Earth ID for Colombia is 23424768.
COLOMBIA_WOE_ID = 23424787

colombia_trends = api.trends_place(COLOMBIA_WOE_ID)

trends = json.loads(json.dumps(colombia_trends, indent=1))

print("Las tendencias más importantes de Colombia son: ")


search_hashtag = tweepy.Cursor(api.search, q="#6402BolsasNegrasDeUribe  filter:images").items(1)
for trend in search_hashtag:
    print(json.dumps(trend._json, indent=2))



# Pedaso Bugeado
# print(sorted(trend._json, key = lambda i: i['retweet_count'],reverse=False))

