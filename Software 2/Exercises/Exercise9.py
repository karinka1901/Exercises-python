import random

#exercise 1
print("------------------------------exercise 1---------------------------------")
class Car:  # type: ignore
    def __init__(self, reg_number, max_speed, current_speed = 0, traveled_distance = 0):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.traveled_distance = traveled_distance

car = Car("ABC-123", 142)
print(f"The registration number of the car is {car.reg_number} and the max speed of the car is {car.max_speed} km/h")

#exercise 2
print("\n------------------------------exercise 2---------------------------------")
class Car:  # type: ignore
    
    def __init__(self, reg_number, max_speed, current_speed = 0, traveled_distance = 0):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.traveled_distance = traveled_distance

    def accelerate (self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0
        
car = Car("ABC-123", 142)
print(f"{car.current_speed} km/h")    
car.accelerate(30)
print(f"{car.current_speed} km/h")   
car.accelerate(70)
print(f"{car.current_speed} km/h")   
car.accelerate(50)
print(f"{car.current_speed} km/h")    #speed is capped at 142
car.accelerate(-200)
print(f"{car.current_speed} km/h")    #speed is reduced to lowest speed of 0

        
#exercise 3
print("\n------------------------------exercise 3---------------------------------")
class Car:  # type: ignore
    
    def __init__(self, reg_number, max_speed, current_speed = 0, traveled_distance = 0):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.traveled_distance = traveled_distance

    def accelerate (self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0
    
    def drive(self, time):
        self.traveled_distance += time * self.current_speed
    
car = Car("ABC-123", 142)
car.accelerate(60)
car.traveled_distance = 2000
print(f"The initial distance is {car.traveled_distance} km/h")
car.drive(1.5)
print(f"The distance traveled in 1.5h at the constant speed of 60 km/h is {car.traveled_distance} km")

#exercise 4
print("\n------------------------------exercise 4---------------------------------")
class Car:
    
    def __init__(self, reg_number, max_speed, current_speed = 0, traveled_distance = 0):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.traveled_distance = traveled_distance

    def accelerate (self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0
    
    def drive(self, time):
        self.traveled_distance += time * self.current_speed

#main
car_list = []
for i in range(1,10):
    new_car = Car("ABC-" + str(i), random.randint(100,200))
    car_list.append(new_car)

race_on = True

while race_on:
    for car in range (len(car_list)):
        if car_list[car].traveled_distance <= 10000:
            car_list[car].drive(1)
            car_list[car].accelerate(random.randint(-10,15))
        else: 
            print(f"The car {car_list[car].reg_number} won the race!!")
            race_on = False
print("registration number, distance traveled, max speed:")
for car in range(len(car_list)):
    print(f"{car_list[car].reg_number}                {car_list[car].traveled_distance} km            {car_list[car].max_speed} km/h")




