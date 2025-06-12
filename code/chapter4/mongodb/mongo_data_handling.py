from pymongo import MongoClient
client = MongoClient('mongodb://admin:secret123@127.0.0.1:27017/local?authSource=admin')
db = client['local']
tweets = db['tweets']

tweet = {
  "_id": 3,
  "usuario": {
    "nick": "herminia",
    "seguidores": 5320
  },
  "texto": "RT:@herminia: hoy,excursión a la sierra con @aniceto!",
  "menciones": [
    "herminia",
    "aniceto"
  ],
  "RT": True,
  "origen": 1
}

inserted = tweets.insert_one(tweet)
if inserted.acknowledged:
    print(f"Tweet inserted with id: {inserted.inserted_id}")
# Retrieve the tweet
retrieved_tweet = tweets.find_one({"_id": 3})
if retrieved_tweet:
    print(f"Retrieved tweet: {retrieved_tweet}")
else:
    print("Tweet not found.")