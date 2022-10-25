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
    sql += " WHERE airport.ident='" + ICAO + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The name of the airport is {row[1]} and it is located in {row[0]}")
            return

ICAO = input("Enter ICAO code: ")
getAirport(ICAO)


#ex2
# Write a program that asks the user to enter the area code (for example FI) 
# and prints out the airports located in that country ordered by airport type. 
# For example, Finland has 65 small airports, 15 helicopter airports and so on.
# print("------------------exercise 2--------------------")

# def get_country (area_code):
#     sql = "SELECT airport.name FROM airport"
#     sql += " WHERE airport.iso_country='" + area_code + "'"
#     #print(sql)
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     if cursor.rowcount > 0:
#         for row in result:
#             print(f"The name of the airport is {row[1]}")
#             return
 

# area_code = input("Enter the area code: ")