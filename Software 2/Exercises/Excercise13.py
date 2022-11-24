from flask import Flask, request, Response
import json
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1',
         autocommit=True
         )


#exercise1
app = Flask(__name__)
@app.route('/prime_number/<number>')
def prime_number(number):
    isPrime = True
    number = int(number)
    if number > 1:
        for i in range (2, number):
            if (number % i) == 0:
                isPrime = False
                break
           

    response = {
        "isPrime" : isPrime,
        "Number" : number
    }
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)


# #exercise2
# app = Flask(__name__)
# @app.route('/airport/<ICAO>')
# def airport (ICAO):
#     sql = "SELECT name, municipality FROM airport"
#     sql += " WHERE ident='" + ICAO + "'"
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     if cursor.rowcount > 0:
#         for row in result:
#             name = row[0]
#             location = row[1]

#     response = {
#         "Airport" : name,
#         "Location" : location,
#         "ICAO" : ICAO
#     }
#     return response

# if __name__ == '__main__':
#     app.run(use_reloader=True, host='127.0.0.1', port=5000)




        
