#ex1
print('Exercise 1:')
num = int(1)
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num = num + 1

#ex2 - method 1:
print('Exercise 2')
inch = float(input("Enter the number in inches: "))
inch_cm = 2.54 * inch
while inch >= 0:
    print(str(inch_cm) + ' cm')
    inch = float(input("Enter the number in inches: "))
