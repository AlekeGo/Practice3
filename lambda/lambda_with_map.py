# Example 1
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  

# Example 2
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x*2, numbers))
print(doubled)  
# Example 3
words = ["apple", "banana", "cherry"]
uppercase_words = list(map(lambda x: x.upper(), words))
print(uppercase_words)  

# Example 4
numbers = [1, 2, 3, 4]
plus_five = list(map(lambda x: x + 5, numbers))
print(plus_five)  

# Example 5
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
sum_lists = list(map(lambda x, y: x + y, numbers1, numbers2))
print(sum_lists)  
