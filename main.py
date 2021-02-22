# -*- coding: utf-8 -*-
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

colombia_trends = api.trends_place(COLOMBIA_WOE_ID, wait_on_rate_limit=True)

trends = json.loads(json.dumps(colombia_trends, indent=1))

print("Las tendencias más importantes de Colombia son: ")


search_hashtags = tweepy.Cursor(
    api.search, q="#6402BolsasNegrasDeUribe  filter:images", result_type="popular").items()
for trend in search_hashtags:
    res = trend._json
    print(f"TEXTO: {res['text']} "
          f"RETWEET COUNT: {res['retweet_count']} "
          f"FAVORITE COUNT: {res['favorite_count']}")
    print("@" * 100, "\n")

print("Exit")
