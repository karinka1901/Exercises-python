def hello():
    print("Hello World!")
    for i in range(5):
        print("-----------")
    print("Goodbye world!")
    return

def minus(argument):
    if argument > 0:
        return - argument
    else:
        return argument

hello() #calls the function
print("blah blah")
hello()

