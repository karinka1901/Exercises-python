#exercise1
import random


print("---------------exercise1---------------------")

class Elevator:  # type: ignore
    def __init__(self, bottom_floor, top_floor,):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = bottom_floor
    
    def floor_up(self, current_floor):
        current_floor += 1

    def floor_down(self, current_floor):
        current_floor -= 1

    def go_to_floor(self, number):
        while number != self.current_floor:
            if number > self.top_floor:
                print("This floor doesn't exist")
                break
            if number < self.bottom_floor:
                print("This floor doesn't exist")
                break
            else:
                if number > self.current_floor:
                    self.floor_up(number)
                    self.current_floor = number
                    print(f"Floor {self.current_floor}")
                    break
                if number < self.current_floor:
                    self.floor_down(number)
                    self.current_floor = number
                    print(f"Floor {self.current_floor}")
                    break
        else:
            print(f'You are already on the {self.current_floor} floor')
            

e = Elevator(1,7)
e.go_to_floor(0) # doesn't exist
e.go_to_floor(8) # doesnt't exist
e.go_to_floor(7)  
e.go_to_floor(3)
e.go_to_floor(3) # already on this floor


#exercise2
print("\n---------------exercise2---------------------")
class Elevator: # type: ignore
    def __init__(self, bottom_floor, top_floor,):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = bottom_floor
    
    def floor_up(self, current_floor):
        current_floor += 1

    def floor_down(self, current_floor):
        current_floor -= 1

    def go_to_floor(self, number):
        while number != self.current_floor:
            if number > self.top_floor:
                print("This floor doesn't exist")
                break
            if number < self.bottom_floor:
                print("This floor doesn't exist")
                break
            else:
                if number > self.current_floor:
                    self.floor_up(number)
                    self.current_floor = number
                    print(f"Going to floor {self.current_floor}")
                    break
                if number < self.current_floor:
                    self.floor_down(number)
                    self.current_floor = number
                    print(f"Going to floor {self.current_floor}")
                    break
        else:
            print(f'You are already on the {self.current_floor} floor')

class Building: # type: ignore
    def __init__(self, bottom_floor, top_floor, numberof_elevators):
        self.elevators = []
        for i in range(numberof_elevators):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number >= 0 and elevator_number < len(self.elevators):
            self.elevators[elevator_number].go_to_floor(destination_floor)
            print(f"The elevator number {elevator_number} is on the floor {self.elevators[elevator_number].current_floor}")
        else:
            print(f"This elevator {elevator_number} doesn't exist!")


        
#main
building = Building(0,7,5)
print(f"There are {len(building.elevators)} elevators in this building")
building.run_elevator(1,3)
building.run_elevator(4,7)
building.run_elevator(5,7)

#exercise3
print("\n---------------exercise3---------------------")
class Elevator: 
    def __init__(self, bottom_floor, top_floor,):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = bottom_floor
    
    def floor_up(self, current_floor):
        current_floor += 1

    def floor_down(self, current_floor):
        current_floor -= 1

    def go_to_floor(self, number):
        while number != self.current_floor:
            if number > self.top_floor:
                print("This floor doesn't exist")
                break
            if number < self.bottom_floor:
                print("This floor doesn't exist")
                break
            else:
                if number > self.current_floor:
                    self.floor_up(number)
                    self.current_floor = number
                    break
                if number < self.current_floor:
                    self.floor_down(number)
                    self.current_floor = number
                    break

class Building:
    def __init__(self, bottom_floor, top_floor, numberof_elevators):
        self.elevators = []
        for i in range(numberof_elevators):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number >= 0 and elevator_number < len(self.elevators):
            self.elevators[elevator_number].go_to_floor(destination_floor)
            print(f"The elevator number {elevator_number} is on the floor {self.elevators[elevator_number].current_floor}")
        else:
            print(f"This elevator {elevator_number} doesn't exist!")


    def fire_alarm(self):
        print("\nWEEE WOOO FIREEEE!\n")
        for i in range(len(self.elevators)):
            self.elevators[i].go_to_floor(self.elevators[i].bottom_floor)
            print(f"The elevator number {i} is on the floor {self.elevators[i].current_floor}")

building = Building(1,8,6)
building.run_elevator(0,8)
building.run_elevator(1,7)
building.run_elevator(2,5)
building.run_elevator(3,4)
building.run_elevator(4,3)
building.run_elevator(5,6)
building.run_elevator(6,2)

building.fire_alarm()


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

# while race.race_finished() == False: #(method2)
#     race.hour_passes()



    
    
    




