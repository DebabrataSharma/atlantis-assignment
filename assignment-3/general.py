from math import radians, cos, sin, asin, sqrt, atan2,pi
from config import *

def split_coordinates(city1_coordinate,city2_coordinate):
    '''
        split the coordinates of both cities and store in an array
    '''
    city1_arr = city1_coordinate.split(", ")
    city2_arr = city2_coordinate.split(", ")
    result = transform_coordinates(city1_arr, city2_arr)
    return result

def transform_coordinates(city1_arr,city2_arr):
    '''
        transform coordinates as positive or negative values
        latitude - North -> positive
                   South -> negative
        longitutes - East -> positive
                     West -> negative
    '''
    try:
        city1_lat = transform_latitude(city1_arr[0])
        city2_lat = transform_latitude(city2_arr[0])
        city1_lon = transform_longitude(city1_arr[1])
        city2_lon = transform_longitude(city2_arr[1])
    except Exception as e:
        return None
    if not city1_lat or not city1_lon or not city2_lat or not city2_lon:
        return None
    distance = calc_distance(city1_lat,city1_lon,city2_lat,city2_lon)
    return distance

def transform_latitude(latitude):
    return radians(float(latitude[:-2])) if latitude[-1].lower()=="n"\
                else radians(-float(latitude[:-2]))  if latitude[-1].lower()=="s"\
                    else None

def transform_longitude(longitude):
    return radians(float(longitude[:-2])) if longitude[-1].lower()=="e"\
                else radians(-float(longitude[:-2]))  if longitude[-1].lower()=="w"\
                    else None


def calc_distance(city1_lat,city1_lon,city2_lat,city2_lon):
    '''
        calculate distance between two cities using Haversine formula
    '''
    dist_lon = (city2_lon - city1_lon)
    dist_lat = (city2_lat - city1_lat)

    a = (pow(sin(dist_lat / 2), 2) +
         pow(sin(dist_lon / 2), 2) *
             cos(city1_lat) * cos(city2_lat))
    radius = r_earth
    c = 2 * asin(sqrt(a))
    return radius * c

def distance_cities(city1_coordinate,city2_coordinate):
    dist = split_coordinates(city1_coordinate,city2_coordinate)
    return dist
