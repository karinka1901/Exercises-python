import random
# #ex1
print('--------Exercise 1:--------')
num = int(1)
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num = num + 1
#
# #ex2:
print('--------Exercise 2--------')
inch = float(input("Enter the number in inches: "))
inch_cm = 2.54 * inch
while inch >= 0:
    print(str(inch_cm) + ' cm')
    inch = float(input("Enter the number in inches: "))
#
# #ex3
print("--------Exercise 3--------")
smallest_num = 0
biggest_num = 0
while True:
    number = input("Enter the number: ")
    if number == "":
        print("The smallest number is " + str(smallest_num))
        print("The biggest number is " + str(biggest_num))
        break
    number_float = float(number)
    if number_float < smallest_num:
        smallest_num = number_float
    if number_float > biggest_num:
        biggest_num = number_float

# #ex3 - second method
# print("--------Exercise 3 -Second method--------")
# numlist = []
# while True:
#     number = input("Enter the number: ")
#     if number == "":
#         print("The smallest number is " + str(min(numlist)))
#         print("The biggest number is " + str(max(numlist)))
#         break
#     numlist.append(float(number))

#ex4
print("--------Exercise 4--------")
number = random.randint(1,10)
#print(number) - testing
while True:
    guess = int(input("Guess the number: "))
    if guess > number:
        print("Too high! Try again!")
    if guess < number:
        print("Too low! Try again!")
    if guess == number:
        print('Correct!')
        break

#ex5
print("--------Exercise 5--------")
username = "python"
password = "rules"
attempts = 4
while attempts >= 0:
    ask_username = input("Enter the username: ")
    ask_password = input("Enter the password:")
    
    if ask_username == username and ask_password == password:
        print("Welcome!")
        break
    if ask_username != username or ask_password != password:
        print("Try again! " + str(attempts) + " attempts remaining.")
        attempts -= 1
        if attempts < 0:
            print("Access denied!")
            break

#ex6
print("--------Exercise 6--------")
    



    
    

