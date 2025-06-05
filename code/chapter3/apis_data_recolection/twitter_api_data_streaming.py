import tweepy
import json

ACCESS_TOKEN = 'ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'ACCESS_SECRET_TOKEN'
CONSUMER_KEY = 'API_KEY'
CONSUMER_SECRET = 'API_SECRET_KEY'

class MyStreamListener(tweepy.StreamListener):
    
    def __init__(self, api=None, ruta=None):
        super(MyStreamListener, self).__init__(api)
        self.fich = open(ruta, 'a', encoding='utf-8') if ruta else None
    
    def on_status(self, status):
        self.fich.write(f"{json.dumps(status._json)}\n")

    def on_error(self, status_code):
        self.fich.close()
        if status_code == 420:
            print("Rate limit exceeded. Disconnecting the stream.")
            return False

ruta_datos = 'data/streaming_tweets.json'
auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
MyStreamListener = MyStreamListener(api= api, ruta=ruta_datos)
flujo = tweepy.Stream(auth=api.auth, listener=MyStreamListener)
try:
    flujo.filter(track=['Petro'], languages=['es'], is_async=True)
    print("Streaming started. Listening for tweets...")  
except Exception as e:
    print(f"Error starting stream: {e}")