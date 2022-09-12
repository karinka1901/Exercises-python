# #ex1
# print("---------------------------Exercise1-----------------------")
# seasons = ("Spring", "Summer", "Autumn", "Winter")
# userinput = int(input("Enter the number of a month to see what season it is: "))
# if userinput > 2 and userinput < 6:
#     #print("The season is: " + str(seasons[0]))
#     print(f"The season is: {seasons[0]}")
# elif userinput > 5 and userinput < 9:
#     print(f"The season is: {seasons[1]}")
# elif userinput > 8 and userinput < 12:
#     print(f"The season is: {seasons[2]}")
# elif (userinput > 0 and userinput < 3) or userinput == 12:
#     print(f"The season is: {seasons[3]}")
# else:
#     print("Invalid month")

#ex2
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

   