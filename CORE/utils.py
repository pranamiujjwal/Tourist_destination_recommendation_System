#!/usr/bin/env python3

#################### ALWAYS RUN THIS FILE FIRST ####################
import pandas as pd
from sklearn.cluster import KMeans

# # load cities coordinates (*BACKUP only if citiesCoordinate.csv is not available*)
# data = {"location":[],"Latitude":[],"Longitude":[]}
# with open("CORE/static/CORE/coordinates.csv", "r") as f:
#   for line in f.readlines():
#     line=line.strip("\n").split(",")
#     data["location"].append(line[1].strip('"'))
#     data["Latitude"].append(line[-2])
#     data["Longitude"].append(line[-1])
# city_dataset = pd.DataFrame(data)
# city_dataset.to_csv("CORE/static/CORE/citiesCoordinate.csv", index=False)

city_dataset = pd.read_csv("CORE/static/CORE/citiesCoordinate.csv")

l2 = city_dataset.iloc[:,-1:-3:-1]
# # print(l2)

# # group around major 50 cities of india
kmeans = KMeans(n_init=200, n_clusters=50, random_state=42)
kmeans.fit(l2)

identified_clusters = kmeans.fit_predict(l2)
identified_clusters = list(identified_clusters)

city_dataset['loc_clusters'] = identified_clusters



restaurants_dataset = pd.read_csv("CORE/static/CORE/Restaurants.csv")

r2 = restaurants_dataset.iloc[:,-1:-3:-1]

# # group around major 50 cities of india
kmeans = KMeans(n_init=200, n_clusters=10, random_state=42)
kmeans.fit(r2)

identified_restaurants_clusters = kmeans.fit_predict(r2)
identified_restaurants_clusters = list(identified_restaurants_clusters)

restaurants_dataset['rest_clusters'] = identified_restaurants_clusters
################################################################################


def getRestaurantsList(city):
  result = []
  try:
    input_city = city.capitalize()
    cluster = restaurants_dataset.loc[restaurants_dataset['location'] == input_city, 'rest_clusters']
    cluster = cluster.iloc[0]
    # # print(cluster)

    restaurants = restaurants_dataset.loc[restaurants_dataset['rest_clusters'] == cluster, ['location','name','place']]
    # print(restaurants)
    # print(len(restaurants))

    for idx in range(len(restaurants)):
      if restaurants.iloc[idx][0] == input_city:
        continue
      else:
        result.append([restaurants.iloc[idx][1],restaurants.iloc[idx][2]])
  except:
    pass
  return result


def getCityList(city):
  result = []
  try:
    input_city = city.capitalize()
    cluster = city_dataset.loc[city_dataset['location'] == input_city, 'loc_clusters']
    cluster = cluster.iloc[0]
    # # print(cluster)

    cities = city_dataset.loc[city_dataset['loc_clusters'] == cluster, 'location']
    # print(cities)
    # print(len(cities))

    for c in range(len(cities)):
      if cities.iloc[c] == input_city:
        continue
      else:
        result.append(cities.iloc[c])
        # print(cities.iloc[c])
  except:
    pass
  return result

