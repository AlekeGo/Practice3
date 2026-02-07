# Example 1
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()


# Example 2
class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()


# Example 3
class Student(Person):
    def __init__(self, fname, lname):
        pass


# Example 4
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


# Example 5
class Student(Person):
    def __init__(self, fname, lname, year):
        Person.__init__(self, fname, lname)
        self.graduationyear = year

x = Student("Anna", "Smith", 2026)
x.printname()
print(x.graduationyear)
