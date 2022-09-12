# #ex1
print("---------------------------Exercise1-----------------------")
seasons = ("Spring", "Summer", "Autumn", "Winter")
userinput = int(input("Enter the number of a month to see what season it is: "))
if userinput > 2 and userinput < 6:
    #print("The season is: " + str(seasons[0]))
    print(f"The season is: {seasons[0]}")
elif userinput > 5 and userinput < 9:
    print(f"The season is: {seasons[1]}")
elif userinput > 8 and userinput < 12:
    print(f"The season is: {seasons[2]}")
elif (userinput > 0 and userinput < 3) or userinput == 12:
    print(f"The season is: {seasons[3]}")
else:
    print("Invalid month")

# #ex2
print("---------------------------Exercise2-----------------------")
names = set()
while True:
    name = str.lower(input("Enter a name: "))
    if name == "":
        for i in names:   #prints the contents of set 
            print(i)
        break

    nameToCompare = name in names    #nameToCompare returns true if name is in names
    if nameToCompare:
        print("Already exists")
    else:
        print("New name")
        names.add(name)

#ex3
print("---------------------------Exercise3-----------------------")
airports = {"EFHK":"Helsinki Vantaa Airport"}
while True:
   select = int(input("Enter a number for what you would like to do: \n1.Enter airport \n2.Fetch airport information \n3.Quit\nOption: "))
   if select == 1:
      code_airport = input("Enter ICAO code: ")
      name_airport = input('Enter airport: ')
      print("Airport information has been added.\n")
      airports[code_airport] = name_airport
   elif select == 2:
      code_airport = input("Enter ICAO code: ")
      if code_airport in airports:
         print(f"The name of the airports is: {airports[code_airport]}\n")
   elif select == 3:
      break
   else:
      print("Error: Enter a number between 1-3\n")