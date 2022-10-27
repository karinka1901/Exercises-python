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
for i in range(0,10):
    new_car = Car("ABC-" + str(i), random.randint(100,200))
    car_list.append(new_car)

race_on = True

while race_on:
    for car in range (len(car_list)):
        if car_list[car].traveled_distance < 10000:
            car_list[car].drive(1)
            car_list[car].accelerate(random.randint(-10,15))
        else: 
            print(f"The car {car_list[car].reg_number} won the race!!")
            race_on = False
print("registration number, distance traveled, max speed:")
for car in range(len(car_list)):
    print(f"{car_list[car].reg_number}                {car_list[car].traveled_distance} km            {car_list[car].max_speed} km/h")
