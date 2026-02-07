# Example 1
class Mother:
    def skills(self):
        print("Cooking")

class Father:
    def skills(self):
        print("Driving")

class Child(Mother, Father):
    pass

c = Child()
c.skills()  # Output: Cooking (Mother is first parent)


# Example 2
class A:
    def greeting(self):
        print("Hello from A")

class B:
    def greeting(self):
        print("Hello from B")

class C(A, B):
    pass

c = C()
c.greeting()  # Output: Hello from A


# Example 3
class Father:
    def drive(self):
        print("Father can drive")

class Mother:
    def cook(self):
        print("Mother can cook")

class Child(Father, Mother):
    pass

c = Child()
c.drive()
c.cook()


# Example 4
class Class1:
    def method1(self):
        print("Method from Class1")

class Class2:
    def method2(self):
        print("Method from Class2")

class Class3(Class1, Class2):
    pass

obj = Class3()
obj.method1()
obj.method2()


# Example 5
class Person:
    def speak(self):
        print("Person speaking")

class Worker:
    def work(self):
        print("Worker working")

class Engineer(Person, Worker):
    pass

e = Engineer()
e.speak()
e.work()
