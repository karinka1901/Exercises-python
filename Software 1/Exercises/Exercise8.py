import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1',
         autocommit=True
         )
#ex1
# Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name and location (town)
# from the airport database used on this course.


print("------------------exercise 1--------------------")
def getAirport (ICAO):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident='" + ICAO + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The name of the airport is {row[0]} and it is located in {row[1]}")
            return

ICAO = input("Enter ICAO code: ")
getAirport(ICAO)

#ex2
# Write a program that asks the user to enter the area code (for example FI)
# and prints out the airports located in that country ordered by airport type.
# For example, Finland has 65 small airports, 15 helicopter airports and so on.
print("\n------------------exercise 2--------------------")

def get_country (area_code):
    sql = "SELECT name, type FROM airport WHERE iso_country='" + area_code + "' order by type"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The airport located in this area is {row[0]} and the type of the airport is {row[1]}")
        return

area_code = input("Enter area code(ex FI): ")
get_country(area_code)


#ex3
# Write a program that asks the user to enter the ICAO codes of two airports.
# The program prints out the distance between the two airports in kilometers.
# The calculation is based on the airport coordinates fetched from the database.
# Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/.
# Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE,
# write geopy into the search field and finish the installation.
print("\n------------------exercise 3--------------------")
import geopy
from geopy.distance import geodesic
def get_location (area_code):
    location = []
    sql = "SELECT longitude_deg, latitude_deg  FROM airport"
    sql += " WHERE ident='" + area_code + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            location.append(row[1])
            location.append(row[0])
        return location

area_code1 = input("Enter area code of the first airport: ")
area_code2 = input("Enter area code of the second airport: ")
print(f"The distance between the two airports is {geodesic(get_location(area_code1), get_location(area_code2)).kilometers:.6} km")
# print(get_location(area_code1), get_location(area_code2))

