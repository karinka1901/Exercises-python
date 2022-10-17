import random
import math
#exercise1
print("-----------------Exercise1-----------------")
def dice_roll():
    num = random.randint(1,6)
    return num

while True:
    roll_num = dice_roll()
    print(roll_num)
    if roll_num == 6:
        break

#2
print("-----------------Exercise2-----------------")
def dice_roll(a):
    num = random.randint(1,a)
    return num

q = int(input("How many sides does the dice have?: "))
while True:
    roll_num = dice_roll(q)
    print(roll_num)
    if roll_num == q:
        break
    
#3
print("-----------------Exercise3-----------------")
def converter(gallons):
#3,78541
    liter = 3.78541 * gallons
    return liter

while True:
    q = int(input("Enter gallons to convert: "))
    if q < 0:
        break
    print(str(converter(q)) + " liters")

#4
print("-----------------Exercise4-----------------")
def sum_of_list(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

number = [23, 7, 10]
print(sum_of_list(number))

#5
print("-----------------Exercise5-----------------")
def remove_uneven(list):
    uneven = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            uneven.append(list[i])
    return uneven


number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number)
print(remove_uneven(number))

#6
print("-----------------Exercise6-----------------")
def pizza_value(d,cost):
    pizza_area = float((math.pi * ((d/2) ** 2))) # in cm^2
    price_per_unit = (10000 * cost) / pizza_area # cost per m^2
    return price_per_unit
d = float(input("Enter the diameter of the first pizza: "))
cost = float(input("Enter the price of the first pizza: "))
first_pizza = pizza_value(d,cost)
print("The cost of the first pizza is " + f"{str(first_pizza):.6}" + " eur per square meter.")
d = float(input("Enter the diameter of the first pizza: "))
cost = float(input("Enter the price of the first pizza: "))
second_pizza = pizza_value(d,cost)
print("The cost of the second pizza is " + f"{str(second_pizza):.6}" + " eur per square meter.")

if first_pizza > second_pizza:
    print("The second pizza is cheaper.")
if second_pizza > first_pizza:
    print("The first pizza is cheaper.")
if second_pizza == first_pizza:
    print("Both pizzas cost the same.")
