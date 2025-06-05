import tweepy

BEARER_TOKEN = 'BEARER_TOKEN'

client = tweepy.Client(bearer_token=BEARER_TOKEN)
response = client.search_recent_tweets(query="Petro", max_results=10)
for tweet in response.data:
    print(tweet.text)