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