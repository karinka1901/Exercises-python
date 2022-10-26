#ex1
print("------------------------exercise 1--------------------------")
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
print("---------------------exercise 2-----------------------------")
