import geopy
from geopy.distance import geodesic
# longitude_deg
# latitude_deg

first = (38.704022, -101.473911)
second = (59.947733, -151.692524)
print(geodesic(first, second).miles)
# 538.390445368
