import tweepy
import json

consumer_key = "4C01PjIV6cXsmGw6p6N0SoRuE"
consumer_secret = "KNiyMxTrtzwxDRljlqNfJTZIOqAbCgTq1jdNvWk86BKvxVv2vY"
access_token = "917511810688999424-wuhA3qMtQ0aqywjcNKvbfc6IU4i65VD"
access_token_secret = "OuwBWadPlNFw5XbRfZFDGcIFygi6DzumtAkf4rEpFjmKx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Publicar Twits

#api.update_status("¡Este twit es Genial! Sin duda alguna Merece Una Camiseta, ¡Aquí la tienes! ")
data = api.me()

ultimo_tweet_id = data._json["status"]["id"]
ultimo_tweet = data._json
print(ultimo_tweet)
#api.create_favorite(ultimo_tweet_id)
#api.retweet(ultimo_tweet_id)
data_img = api.media_upload("./images/mono.jpeg")
print (data_img)
image_data = data_img.media_id
print(image_data)
api.update_status("¡Este twit es Genial! Sin duda alguna Merece Una Camiseta, ¡Aquí la tienes!", in_reply_to_status_id=1364079951759171585,  media_ids=[image_data])