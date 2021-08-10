'''
    Write a python class that is able to return the flight distance between two cities given their latitude and longitude coordinates. 

'''

from general import *

if __name__=="__main__":
    city1_coordinate = input("City 1: ")
    city2_coordinate = input("City 2: ")
    distance = distance_cities(city1_coordinate,city2_coordinate)
    if distance:
        print("City 1 and City 2 are " +str(distance)+" km apart")
    else:
        print("Invalid input, please try again. Input for each city should be in 'latitude<space><N/S>,<space>longitude<space><E/W>'")
