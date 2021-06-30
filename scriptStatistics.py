import json
import pymongo
import tweepy
import pandas as pd
from io import open
from matplotlib import pyplot as plt
from numpy import array

def getStatistics():
        
    my_client = pymongo.MongoClient(
        'mongodb+srv://grupo03DB:X1clTzhtGdZYCP9G@jdcluster-almnw.gcp.mongodb.net/Tweets?retryWrites=true&w=majority')
    my_database = my_client.Tweets
    my_collection = my_database.collectionTweets

    my_cursor = my_collection.find({}, {"sentimiento": 1})

    arreglo1 = []
    arreglo2 = []
    arreglo3 = []

    for item in my_cursor:
        if(len(item) == 2):
            if(item["sentimiento"] > 0.6):
                arreglo1.append(item["sentimiento"])
            elif(item["sentimiento"] < 0.4):
                arreglo2.append(item["sentimiento"])
            elif(item["sentimiento"] >= 0.4 and item["sentimiento"] <= 0.6):
                arreglo3.append(item["sentimiento"])

    print("\nPOSITIVOS >0.6")
    df1 = pd.DataFrame(arreglo1)
    plt.plot(arreglo1)
    plt.ylabel("Sentimiento")
    plt.xlabel("Cantidad")
    plt.show()
    print(df1.describe())

    print("\nNEUTRAL  0.4 - 0.6")
    if not arreglo3:
        print("No hay valores neutrales")
    else:
        df3 = pd.DataFrame(arreglo3)
        print(df3.describe())

    print("\nNEGATIVO <0.4")
    df2 = pd.DataFrame(arreglo2)
    plt.plot(arreglo2)
    plt.ylabel("Sentimiento")
    plt.xlabel("Cantidad")
    plt.show()
    print(df2.describe())