"""
Python Program to Demonstrate the Use of the map() Function
Basic Examples
"""

# Example 1: Using map() with a normal function
def square(num):
    return num * num

numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print("Squares:", squared)

# Example 2: Using map() with lambda
numbers2 = [10, 20, 30]
doubled = list(map(lambda x: x * 2, numbers2))
print("Doubled:", doubled)

# Example 3: Mapping multiple iterables
l1 = [1, 2, 3]
l2 = [4, 5, 6]
summed = list(map(lambda x, y: x + y, l1, l2))
print("Sum of two lists:", summed)
