# import mysql.connector
# def getEmployeesByLastName(last_name):
#     sql = "SELECT sukunimi, etunimi, palkka FROM tyontekija"
#     sql += " WHERE sukunimi='" + last_name + "'"
#     print(sql)
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     if cursor.rowcount >0 :
#         for row in result:
#             print(f"Hello! I'm {row[1]} {row[0]}. My salary is {row[2]} euros per month.")
#     return

# connection = mysql.connector.connect(
#          host='127.0.0.1',
#          port= 3306,
#          database='ihmiset',
#          user='root',
#          password='1',
#          autocommit=True
#          )
         
# last_name = input("Enter last name: ")
# getEmployeesByLastName(last_name)
         
#1
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1',
         autocommit=True
         )

mycursor = connection.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
  