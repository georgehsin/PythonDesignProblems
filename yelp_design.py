# Build a simple Yelp-like system: Given a set of restaurant and metadata (coordinates, ratings, opening hours), design and implement the following functionalities without using a database.

# 1. Find restaurants within specified radius, given a coordinate
# 2. Improve the above function by only returning restaurants that are open given desired dining hour
# 3. Improve the above function by sorting the results by average ratings
import math
from operator import itemgetter

class Yelp(object):
	def __init__(self, restaurants, ratings):
		self.restaurants = restaurants
		self.ratings = ratings

	def find(self, coordinates, radius, dining_hour=None, sort_by_rating=False):
        # Returns list of Restaurant within radius.
        #
        #  coordinates: (latitude, longitude)
        #  radius: kilometer in integer
        #  dining_hour: If None, find any restaurant in radius.
        #               Otherwise return list of open restaurants at specified hour.
        #  sort_by_rating: If True, sort result in descending order,
        #                  highest rated first.

		filtered = []
		for r in self.restaurants:
			length = abs(r.latitude-coordinates[0])**2
			height = abs(r.longitude-coordinates[1])**2
			if math.sqrt(length+height) <= 5:
				if dining_hour != None:
					if dining_hour > r.open_hour and dining_hour < r.close_hour:
						if sort_by_rating:
							filtered.append((r,self.ratings[r.id].rating))
						else:
							filtered.append(r)
					else:
						continue
				else:
					if sort_by_rating:
						filtered.append((r,self.ratings[r.id].rating))
			else:
				filtered.append(r)
		if sort_by_rating:
			filtered.sort(key=itemgetter(1))
			return filtered
		return filtered
		raise NotImplementedError("please implement")

class Restaurant(object):
    # where open_hour and close_hour is in [0-23]
    def __init__(self, id, name, latitude, longitude, open_hour, close_hour):
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.open_hour = open_hour
        self.close_hour = close_hour
        

class Rating(object):
    # rating is in [1-5]
    def __init__(self, restaurant_id, rating):
        self.restaurant_id = restaurant_id
        self.rating = rating

def main():
    restaurants = [
    	Restaurant(0, "Domino's Pizza", 37.7577, -122.4376, 7, 23),
    	Restaurant(1, "Papa John's Pizza", 37.7577, -122.4376, 16, 20),
    	Restaurant(2, "Caesar's Pizza", 37.7577, -122.4376, 8, 23),
    	Restaurant(3, "Pizza Hut Pizza", 37.7577, -122.4376, 1, 12) 
    	]
    ratings = [
    	Rating(0, 3), 
    	Rating(0, 5), 
    	Rating(0, 4), 
    	Rating(0, 1), 
    	]

    y = Yelp(restaurants, ratings)
    results = y.find((37.7, -122.6), 5, 15, False)
    print results.sort_by_rating
    for i in results:
        print i[0].name

main()
