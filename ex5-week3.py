import random


# #ex1
# print("----------------exercise 1------------------")
# times_to_roll = input("How many dice to roll? ")
# sum_dice = 0

# for dice_roll in range(int(times_to_roll)):
#     random_dice = random.randint(1,6) 
#     #print(random_dice) testing
#     sum_dice += random_dice
# print(sum_dice)

# #ex2
# print("----------------exercise 2------------------")
# numbers = []
# while True:
#     number = input("Enter the number: ")
#     if number == "":
#         numbers.sort(reverse=True)
#         print(numbers[:5])
#     numbers.append(int(number))

#ex3
print("----------------exercise 3------------------")
divisible_numbers = []
number = int(input("Enter the number"))
for x in range(1,number):
    divisible_numbers.append(number)
    number % x == 0

