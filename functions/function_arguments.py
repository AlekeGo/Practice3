# Example 1
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# Example 2
def my_function(name):
    print("Hello", name)

my_function("Emil")


# Example 3
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")


# Example 4
def my_function(name = "friend"):
    print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")


# Example 5
def my_function(country = "Norway"):
    print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
