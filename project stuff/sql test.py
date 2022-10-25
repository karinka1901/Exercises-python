# from continent_game_function import *
# from Functions import *
import os
import mysql.connector
import time
import sys
import os
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='1',
         autocommit=True
         )


def typewriter(rules):
    for char in rules:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != "\n":
            time.sleep(0.02)
        else:
            time.sleep(1)



def cheat_sheet():
    countrylist = [['Andorra  ', 'Albania  ', 'Austria  ', 'Belgium  ', 'Slovakia ', 'Bulgaria ', 'Belarus  ',
                    'Serbia   ', 'Sweden   ', 'Germany  ', 'Denmark  ', 'Estonia  ', 'Spain    ', 'Finland  ',
                    'Romania  '], ['France     ', 'Ukraine    ', 'Guernsey   ', 'Gibraltar  ', 'Greece     ',
                    'Croatia    ', 'Hungary    ', 'Ireland    ', 'Monaco     ', 'Iceland    ', 'Italy      ',
                    'Jersey     ', 'Russia     ', 'Lithuania  ', 'Luxembourg '], ['Latvia      ', 'Isle of Man ',
                    'Moldova     ', 'Montenegro  ', 'Kosovo      ', 'Malta  ','Netherlands  ', 'Norway  ', 'Poland  ',
                    'Portugal  ', 'Faroe Islands  ', 'Switzerland  ', 'Liechtenstein  ', 'Czech Republic  ',
                    'Slovenia  '],['Bosnia and Herzegovina  ', 'San Marino  ', 'United Kingdom  ', 'Vatican City  ',
                    'North Macedonia  ', '', '', '', '', '', '', '', '', '', '']]
    print("\nCHEAT SHEET, MAKE SURE TEACHER DOESN'T SEE YOU!!!")
    for x, y, z, q in zip(*countrylist):
        print(x, y, z, q)

def credits_text():
    credits = "Designed and developed by Group 2\nKarin Domagalska\nJoona Rantala\nCan Erman\nNadim Ahmed"
    typewriter(credits)
    print("\n")


def easter_egg():
    while True:
        egg = input("\nyes or no: ")
        if egg == "yes":
            egg = input("\nyes or no: ")
            if egg == "yes":
                egg = input("\nyes or no: ")
                if egg == "yes":
                    egg = input("\nyes or no: ")
                    if egg == "yes":
                        print(f"\n\n\n\U0001F49A\U0001F49APlease grade us 5/5\U0001F49A\U0001F49A\n\n\n")
                        break
                    elif egg == '1':
                        print("\n")
                        break
                    elif egg == "no":
                        print("Wrong answer.")
                elif egg == '1':
                    print("\n")
                    break
                elif egg == "no":
                    print("Wrong answer.")
            elif egg == '1':
                print("\n")
                break
            elif egg == "no":
                print("Wrong answer.")
        elif egg == '1':
            print("\n")
            break
        elif egg == "no":
            print("Wrong answer.")


print("""\                                                                                                
 .d8888b.  888     888  .d8888b. 88888888888     d8888 8888888 888b    888      88888888888 888    888 8888888888      8888888b.  888             d8888 888b    888 8888888888 
d88P  Y88b 888     888 d88P  Y88b    888        d88888   888   8888b   888          888     888    888 888             888   Y88b 888            d88888 8888b   888 888        
Y88b.      888     888 Y88b.         888       d88P888   888   88888b  888          888     888    888 888             888    888 888           d88P888 88888b  888 888        
 "Y888b.   888     888  "Y888b.      888      d88P 888   888   888Y88b 888          888     8888888888 8888888         888   d88P 888          d88P 888 888Y88b 888 8888888    
    "Y88b. 888     888     "Y88b.    888     d88P  888   888   888 Y88b888          888     888    888 888             8888888P"  888         d88P  888 888 Y88b888 888        
      "888 888     888       "888    888    d88P   888   888   888  Y88888          888     888    888 888             888        888        d88P   888 888  Y88888 888        
Y88b  d88P Y88b. .d88P Y88b  d88P    888   d8888888888   888   888   Y8888          888     888    888 888             888        888       d8888888888 888   Y8888 888        
 "Y8888P"   "Y88888P"   "Y8888P"     888  d88P     888 8888888 888    Y888          888     888    888 8888888888      888        88888888 d88P     888 888    Y888 8888888888 
  """)

while True:
    print("\nWelcome to Green Wash Airlines")
    main_menu = int(input("1. Continent game \n2. Europe game \n3. Credits \n4. Something funny. \n5. Quit\n"))
    if main_menu == 1:
        print("something")
    elif main_menu == 2:
        while True:
            eu_menu = int(input("\nEU game\n1. Start \n2. Country cheat sheet. \n3. Back \n"))
            if eu_menu == 1:
                print("function here")
            elif eu_menu == 2:
                cheat_sheet()
            elif eu_menu == 3:
                break
    elif main_menu == 3:
        credits_text()
    elif main_menu == 4:
        easter_egg()
    elif main_menu == 5:
        typewriter("Exiting the game.")
        break
