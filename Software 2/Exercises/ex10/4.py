import random
#exercise4
print("\n---------------exercise4---------------------")
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


class Race:
    def __init__(self, race_name, distance, cars):
        self.cars = []
        self.cars.extend(cars)
        self.name = race_name
        self.distance = distance
        self.timer = 0

    def hour_passes(self):
        for car in range (len(self.cars)):
            self.cars[car].drive(1)
            self.cars[car].accelerate(random.randint(-10,15))
            if car == 9: #when all cars drove for an hour
                self.timer += 1 #adds another h
            if self.timer % 10 == 0 and car == 9: #will print the status after every 10hours
                print(f"\n{self.timer} hours has passed") 
                self.print_status()

    def print_status(self):
        #print("registration number, distance traveled, max speed:")
        for car in range(len(self.cars)):
            print(f"{self.cars[car].reg_number} {self.cars[car].traveled_distance}km {self.cars[car].max_speed}km/h")

    def race_finished(self):
        for car in range (len(self.cars)):
            if self.cars[car].traveled_distance >= self.distance: #if any of the cars have driven the entire distance of the race
                print(f"\n\nThe car {self.cars[car].reg_number} won the race!!")
                self.print_status()
                return True
            # else:
            #     return False #(method2)

car_list = []
for i in range(0,10):
    new_car = Car("ABC-" + str(i), random.randint(100,200))
    car_list.append(new_car)

#main
race = Race("Grand Demolition Derby", 8000, car_list)
print(f"Welcome to the {race.name} race!")

while not race.race_finished(): # while not True
    race.hour_passes()

# while race.race_finished() == False: #(for the method2)
#     race.hour_passes()

