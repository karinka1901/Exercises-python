#ex1
print("------------------------exercise1-------------------------")
class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_info(self):
        print(f"{self.name} (author {self.author}, {self.page_count} pages)")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)


    def print_info(self):
        print(f"{self.name} (chief editor {self.chief_editor})")


#main
book = Book("Compartment No. 6", "Rosa Liksom", 192)
book.print_info()
magazine = Magazine("Donald Duck", "Aki Hyyppä" )
magazine.print_info()


#ex2
print("---------------------exercise 2----------------------------")

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
        self.traveled_distance += time * self.max_speed
        print(f"{self.reg_number}: {self.traveled_distance} km")


class ElectricCar(Car):
    def __init__(self, reg_number, max_speed, battery_capacity):
        self.battery_capacity = battery_capacity
        super().__init__(reg_number, max_speed)

class GasolineCar(Car):
    def __init__(self, reg_number, max_speed, tank_volume):
        self.tank_volume = tank_volume
        super().__init__(reg_number, max_speed)


#main
electric = ElectricCar("ABC-15", 180, 52.5)
gasoline = GasolineCar("ACD-123", 165, 32.3)
electric.drive(3)
gasoline.drive(3)
