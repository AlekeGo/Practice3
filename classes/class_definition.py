# Example 1
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)


# Example 2
class MyClass:
    x = 5

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)


# Example 3
class Person:
    pass


# Example 4
class MyClass:
    x = 5

p1 = MyClass()
del p1


# Example 5
class MyClass:
    x = 5

p1 = MyClass()
del p1.x
print(MyClass.x)
