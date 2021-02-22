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
WOE_ID = 1


# COUNTRIES WOE_ID


region_trends = api.trends_place(WOE_ID, wait_on_rate_limit=True)

trends = json.loads(json.dumps(region_trends, indent=1))

print("Las tendencias más importantes de la región son: ")
print(f"{trends}  \n")

print("Los Twits más importantes de la tendencia son: \n")
trendingtopic = trends[0]['trends'][3]['name']
search_hashtags = tweepy.Cursor(
    api.search, q=trendingtopic, result_type="popular").items(10)
for trend in search_hashtags:
    res = trend._json
    print(f"TEXTO: {res['text']} "
          f"ID: {res['id']} "
          f"RETWEET COUNT: {res['retweet_count']} "
          f"FAVORITE COUNT: {res['favorite_count']}")
    print("@" * 100 )
    print(f"LINK: https://twitter.com/n/status/{res['id']} \n ")

print("Exit")