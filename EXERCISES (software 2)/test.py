# class Dog:
#     def __init__(self, name, birth_year, sound="Woof woof"):
#         self.name = name
#         self.birth_year = birth_year
#         self.sound = sound

#     def bark(self, times):
#         for i in range(times):
#             print(self.sound)
#         return


# dog1 = Dog("Rascal", 2018)
# dog2 = Dog("Boi", 2022, "Yip yip yip")

# dog1.bark(2)
# dog2.bark(5)

class Car:

    currentSpeed = 0
    distanceTravelled = 0

    def __init__(self, regNumber, maxSpeed):
        self.regNumber = regNumber
        self.maxSpeed = maxSpeed

    def accelerate(self, changeOfSpeed):
        if changeOfSpeed > 0:
            if self.currentSpeed + changeOfSpeed < self.maxSpeed:
                self.currentSpeed += changeOfSpeed
            else:
                self.currentSpeed = self.maxSpeed
        if changeOfSpeed < 0:
            if self.currentSpeed + changeOfSpeed <= 0:      #using + because change of speed is negative
                self.currentSpeed = 0
            else:
                self.currentSpeed -= changeOfSpeed

car = Car("ABC-123", 142)

#3 ways of displaying information 
#print(f"Registration: {firstCar.regNumber}\nMax speed: {firstCar.maxSpeed}\nCurrent speed: {firstCar.currentSpeed}\nDistance travelled: {firstCar.distanceTravelled}")
#print(firstCar.regNumber, firstCar.maxSpeed, firstCar.currentSpeed, firstCar.distanceTravelled)
#pprint(vars(firstCar))

print(f"{car.currentSpeed} km/h")    #speed = 0
car.accelerate(30)
print(f"{car.currentSpeed} km/h")    #speed = 30
car.accelerate(-10)
print(f"{car.currentSpeed} km/h")    #speed = 30