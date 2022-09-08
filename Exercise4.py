import random
#ex1
print('--------Exercise 1:--------')
num = int(1)
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num = num + 1

#ex2:
print('--------Exercise 2--------')
inch = float(input("Enter the number in inches: "))
inch_cm = 2.54 * inch
while inch >= 0:
    print(str(inch_cm) + ' cm')
    inch = float(input("Enter the number in inches: "))
    if inch < 0:
        print("The program has ended")
        
#ex3
print("--------Exercise 3--------")
smallest_num = 0
biggest_num = 0
while True:
    number = input("Enter the number: ")
    if number == "":
        print("The smallest number is " + str(smallest_num))
        print("The biggest number is " + str(biggest_num))
        break
    if smallest_num == 0 and biggest_num == 0:
        if float(number) != 0:
            if float(number) < 0:
                smallest_num = float(number)
            else:
                biggest_num = float(number)
    number_float = float(number)
    if biggest_num < number_float:
        biggest_num = number_float
    if smallest_num > number_float:
        smallest_num = number_float

#ex3
print("--------Exercise 3--------")
numlist = []
while True:
     number = input("Enter the number: ")
     if number == "":
         print("The smallest number is " + str(min(numlist)))
         print("The biggest number is " + str(max(numlist)))
         break
     numlist.append(float(number))

#ex 3  third method:
prompt = "Give the number: "
s = input(prompt)
if s != "":
    smallest =int(s)
    largest = smallest
while s != "":
    n = int(s)
    if n < smallest:
        smallest = n
    if n > largest:
        largest = n
    s = input(prompt)
else:
    print(smallest)
    print(largest)

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
    
    if ask_username != username or ask_password != password:
        print("Wrong credentials! " + str(attempts) + " attempts remaining.")
        attempts -= 1
        if attempts < 0:
            print("Access denied!")
            break
    else:
        print("Welcome!")
        break

#ex6
print("--------Exercise 6--------")
n = 0 #number of points that fall into circle
counter = 0
while True:
    N = int(input('Enter the amount to generate: '))
    while counter <= N:
        x = random.uniform(0,1) #random float position of points that fall into an x-axis
        y = random.uniform(0,1) #same with y-axis
        counter += 1
        if x**2 + y**2 < 1:  
            n += 1   #counter that tracks points that fall into a circle if the inequation is true
    pi_approx = (4*n) / N  #approximation of the value of pi
    print("The approximation of pi is " + str(pi_approx))
    break

