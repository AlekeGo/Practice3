# Example 1
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  

# Example 2
words = ["apple", "banana", "cherry", "kiwi"]
long_words = list(filter(lambda x: len(x) > 4, words))
print(long_words)  

# Example 3
ages = [12, 17, 19, 24, 15]
adults = list(filter(lambda x: x >= 18, ages))
print(adults) 

# Example 4
numbers = [10, 15, 20, 25, 30]
divisible_by_5 = list(filter(lambda x: x % 5 == 0, numbers))
print(divisible_by_5)  

# Example 5
names = ["Tom", "Tim", "Anna", "Bob"]
names_with_t = list(filter(lambda x: x.startswith("T"), names))
print(names_with_t) 
