#ex4 three integers ->the sum, product, average
first_int = input("enter the first number: ")
second_int = input("enter the second number: ")
third_int = input("enter the third number: ")
sum_int = int(first_int) + int(second_int) + int(third_int)
product_int = int(first_int) * int(second_int) * int(third_int)
average_int = ((int(first_int) + int(second_int) + int(third_int)) / 3)

print("the sum is " + str(sum_int))
print("the product is " + str(product_int))
print("the average is " + str(average_int))