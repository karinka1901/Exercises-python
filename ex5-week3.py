# import random


# # #ex1
# # print("----------------exercise 1------------------")
# # times_to_roll = input("How many dice to roll? ")
# # sum_dice = 0

# # for dice_roll in range(int(times_to_roll)):
# #     random_dice = random.randint(1,6) 
# #     #print(random_dice) testing
# #     sum_dice += random_dice
# # print(sum_dice)

# # #ex2
# # print("----------------exercise 2------------------")
# # numbers = []
# # while True:
# #     number = input("Enter the number: ")
# #     if number == "":
# #         numbers.sort(reverse=True)
# #         print(numbers[:5])
# #     numbers.append(int(number))

# #ex3
# print("----------------exercise 3------------------")
# isPrime = False
# number = int(input("Enter the number: "))
# if number > 1:
#     for i in range (2, number):
#         if (number % i) == 0:
#             isPrime = True
#             break
# if isPrime:
#     print(str(number) + " is not a prime number")
# else:
#     print(str(number) + " is a prime number")
    
#ex4
print("----------------exercise 4------------------")
city_names = []

for i in range (1,6):
    city = input("Enter the name of a city: ")
    city_names.append(city)
print(city_names)




