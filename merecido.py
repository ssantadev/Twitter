import status as status
import tweepy
import json


consumer_key = "4C01PjIV6cXsmGw6p6N0SoRuE"
consumer_secret = "KNiyMxTrtzwxDRljlqNfJTZIOqAbCgTq1jdNvWk86BKvxVv2vY"
access_token = "917511810688999424-wuhA3qMtQ0aqywjcNKvbfc6IU4i65VD"
access_token_secret = "OuwBWadPlNFw5XbRfZFDGcIFygi6DzumtAkf4rEpFjmKx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


data_img = api.media_upload("./images/mono.jpeg")
image_data = data_img.media_id

class TweetsListener(tweepy.StreamListener):

    def on_connect(self):
        print("Canal conectado al Hashtag #MereceUnaCamiseta")

    def on_status(self, status):
        print("¡ATENCIÓN! Hemos Recibido un nuevo Twit con el Hashtag #MereceUnaCamiseta")
        print(status.text)
        print("@"*100)
 #       print("Respuesta al Twit con ID: " + status.in_reply_to_status_id)
        print(status.id)
        api.update_status("¡Este twit es Genial! Sin duda alguna Merece Una Camiseta, ¡Aquí la tienes!",
                          in_reply_to_status_id=status.id, media_ids=[image_data],  auto_populate_reply_metadata=True)




    def on_error(self, status_code):
        print("Error", status_code)





# Publicar Tweets
# data = api.me()

#ultimo_tweet_id = data._json["status"]["id"]
#ultimo_tweet = data._json
#print(ultimo_tweet)
#api.create_favorite(ultimo_tweet_id)
#api.retweet(ultimo_tweet_id)




stream = TweetsListener()
streamingApi = tweepy.Stream(auth=api.auth, listener=stream)
streamingApi.filter(
    track=["#MereceUnaCamiseta"],
)


