import folium
import branca
import pymongo
import json
import random
import decimal


def setMaps():

    my_client = pymongo.MongoClient(
        'mongodb+srv://grupo03DB:X1clTzhtGdZYCP9G@jdcluster-almnw.gcp.mongodb.net/Tweets?retryWrites=true&w=majority')

    my_database = my_client.Tweets
    my_collection = my_database.collectionTweets

    list = [1]
    check = True
    my_cursor = my_collection.find({})
    cont = 0
    map = folium.Map(location=(-0.225219, -78.5248), zoom_start=8)

    for item in my_cursor:
        if item["location"] is not False:
            if len(item["location"]["coordinates"]) == 2:
                for x in list:
                    if x == item["text"]:
                        check = False
                        break
                    else:
                        check = True
                if check:
                    list.append(item['location']["coordinates"])
                    cont += 1
                    html = f"<p>Tweet:{item['text']}</p><p>locación:{item['location']['ciudad']}</p><p>Nivel de sentimiento: {item['sentimiento']}</p>"
                    iframe = branca.element.IFrame(
                        html=html, width=500, height=300)
                    lat = float(item["location"]["coordinates"]
                                [1] + round(random.random(), 2)/(10*3))
                    log = float(item["location"]["coordinates"]
                                [0] + round(random.random(), 2)/(10*3))
                    if item['sentimiento'] < 0.5:
                        folium.Marker(
                            location=(lat,
                                      log),
                            popup=folium.Popup(iframe, max_width=500),
                            icon=folium.Icon(color="red")
                        ).add_to(map)
                    elif item['sentimiento'] > 0.5:
                        folium.Marker(
                            location=(lat,
                                      log),
                            popup=folium.Popup(iframe, max_width=500),
                            icon=folium.Icon(color="green")
                        ).add_to(map)
                    else:
                        folium.Marker(
                            location=(lat,
                                      log),
                            popup=folium.Popup(iframe, max_width=500),
                            icon=folium.Icon(color="yellow")
                        ).add_to(map)
    print(cont)
    map.save("index.html")
