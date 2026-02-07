# Example 1
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)

# Example 2
words = ["banana", "apple", "cherry", "date"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

# Example 3
tuples = [(1, 3), (3, 2), (5, 1)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)

# Example 4
numbers = [10, 21, 4, 15, 7]
sorted_desc = sorted(numbers, key=lambda x: x, reverse=True)
print(sorted_desc)

# Example 5
words = ["apple", "Banana", "cherry", "date"]
sorted_ignore_case = sorted(words, key=lambda x: x.lower())
print(sorted_ignore_case)
