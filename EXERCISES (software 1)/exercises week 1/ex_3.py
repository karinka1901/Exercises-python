#("ex3 ask for the lenght and width of a rectangle and print the perimeter, area")
lenght = input("enter the lenght:")
width = input("enter the width:")
parameter = (float(lenght) + float(width)) * 2
area_rec = float(lenght) * float(width)
print("the parameter of the rectangular is " + str(parameter))
print("the area of the rectangular is " + str(area_rec))