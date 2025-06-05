import tweepy

ACCESS_TOKEN = 'ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'ACCESS_SECRET_TOKEN'
CONSUMER_KEY = 'API_KEY'
CONSUMER_SECRET = 'API_SECRET_KEY'

auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
    tweets_list = api.search_tweets(q="Python", count=10)
    tweets_list_json = []
    for tweet in tweets_list:
        tweets_list_json.append(tweet._json)
    print("Tweets fetched successfully")
    print(tweets_list_json)
except Exception as e:
    print("Error during authentication:", e)
