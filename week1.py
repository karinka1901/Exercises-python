


class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []
    

    def add(self, person: Person):
        self.persons.append(person)
        
    def is_empty(self):
        return len(self.persons) == 0

    def print_info(self):
        combined_height = 0
        for person in self.persons:
            combined_height += person.height
        print(f"There are {len(self.persons)} people in the room. Their toatl height is {combined_height} cm")
        for person in self.persons:
            print(f"name: {person.name}, height: {person.height} cm")
        
    """
    def tallest(self):
        if self.is_empty == True:
            return None
        else:
            for person in self.persons:
                max_height = max(person.height)
                return max_height """
      

    def tallest(self):
        max_height = 0
        tallest_person = None
        for person in self.persons:
            if tallest_person is None or person.height > max_height:
                tallest_person = person
                max_height = person.height
        return tallest_person



    def remove_tallest(self):
        tallest_person = self.tallest()
        if tallest_person:
            self.persons.remove(tallest_person)

        return tallest_person

room = Room()
room.add(Person("a", 180))
room.add(Person("b", 170))
room.add(Person("c", 160))
room.add(Person("d", 150))

print(f"is the room empty: {room.is_empty}")
print(f"The tallest: {room.tallest}")

print(room.print_info())

print()
removed = room.remove_tallest()
room.print_info()






        