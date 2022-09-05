print("--------Exercise 3--------")
smallest_num = -1
biggest_num = 1
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