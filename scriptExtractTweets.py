import json
import tweepy
import pymongo
import random
from classifier import SentimentClassifier


def extractTweets():
    print('Preparando para extraer Tweets...')
    my_client = pymongo.MongoClient(
        'mongodb+srv://grupo03DB:X1clTzhtGdZYCP9G@jdcluster-almnw.gcp.mongodb.net/Tweets?retryWrites=true&w=majority')
    my_database = my_client.Tweets
    my_collection = my_database.collectionTweets

    ckey = "I65HkSxcTY22zgzydGmE14pUi"
    csecret = "4gBAWqmerng8tSWzC6YFqxCBCNv03CatcK1EhZh3YY1jzzxHfr"
    atoken = "1268310592496025600-QOhJRE7KRAJY9rYTb5ldUTeWt8Sgt5"
    asecret = "xW8zFoy2RlrdvmtKabDj2kDDPmBHUXvaR3WEnxnHHq0Nf"
    clf = SentimentClassifier()
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    for tweet in tweepy.Cursor(api.search, q="corrupcion -filter:retweets", geocode="-0.225219,-78.5248,500km", tweet_mode="extended").items(2000):
        print(tweet._json["full_text"], "\n")

        if tweet._json["place"] is not None:
            print("**************Con coordenadas**********\n")
            print(json.dumps(tweet._json, indent=2), "\n\n")
            # Con coordenadas para guardar
            decoded = json.loads(json.dumps(tweet._json))
            coordenadas = decoded["place"]["bounding_box"]["coordinates"]
            ciudad = str(decoded["place"]["name"])
            sentimiento = clf.predict(tweet._json["full_text"])
            my_collection.insert_one({
                "text": tweet._json["full_text"],
                "location": {
                    "ciudad": ciudad,
                    "coordinates": coordenadas[0][random.randint(0, 3)]
                },
                "created_at": tweet._json["created_at"],
                "sentimiento": sentimiento
            })
