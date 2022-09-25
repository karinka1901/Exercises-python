
#ex1
# Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name and location (town)
# from the airport database used on this course.
# 

# print("------------------exercise 1--------------------")
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1',
         autocommit=True
         )

def getAirport (ICAO):
    sql = "SELECT name FROM country"
    sql += " WHERE continent='" + ICAO + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f" {row[0]}")
    return

ICAO = input("Enter ICAO code: ")
getAirport(ICAO)