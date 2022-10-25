import math
import random
#ex 1 - ask and print a name
name = input("What is your name? ")
print("Hello, " + name + "!")

#ex2 - ask for a radius and print an area of a circle
radius = float(input("Enter the radius: "))
#area = math.pi * float(radius) ** 2
#print("The area is: " + str(area))
print(f"Area is{math.pi * radius ** 2:10.1f}")

#ex3 - ask for lenght, width of a rectangular and calculate the perimeter and area
lenght = input("Enter the lenght: ")
width = input("Enter the width: ")
perimeter = 2 * float(lenght) + 2 * float(width)
area = float(width) * float(lenght)
print("The perimeter of the rectangular is " + str(perimeter))
print("The area of the rectangular is " + str(area))

#ex4 - ask for 3 numbers and print the sum, product and average
first = input("Enter the first number: ")
second = input("Enter the second number: ")
third = input("Enter the third number: ")
sum = float(first) + float(second) + float(third)
product = float(first) * float(second) * float(third)
average = sum / 3
print("The sum is: " + str(sum))
print("The product is: " + str(product))
print("The average is: " + str(average))

#ex5 - convert medival units to kg and gramms:
talent = input("Enter talents: ")
pounds = input("Enter pounds: ")
lots = input("Enter lots: ")

talent_grams = 20 * 32 * 13.3 * float(talent)
pounds_grams = 32 * 13.3 * float(pounds)
lots_grams = 13.3 * float(lots)

result = talent_grams + pounds_grams + lots_grams
kg = int(result / 1000)
grams = result - kg * 1000

print("The weight in modern units is: " + str(kg) + " kilograms " + f"{str(grams):.6}" + " grams.")

#ex6
print("3-digit code: " + f"{random.randint(0, 999):03d}")
#print(str(random.randint(0,9)) + str(random.randint(0,9) + str(random.randint(0,9)))

print("4-digit code: " + str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6)))
