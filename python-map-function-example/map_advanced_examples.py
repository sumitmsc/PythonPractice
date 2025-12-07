"""
Advanced Python Map() Examples
"""

# Example 4: Cleaning text using map()
texts = [" hello ", " world ", " python "]
cleaned = list(map(lambda x: x.strip().upper(), texts))
print("Cleaned text:", cleaned)

# Example 5: Converting string numbers to integers
string_numbers = ["10", "20", "30", "40"]
converted = list(map(int, string_numbers))
print("Converted to integers:", converted)

# Example 6: map() for temperature conversion
temperatures_c = [0, 20, 37, 100]
def c_to_f(c):
    return (c * 9/5) + 32
fahrenheit = list(map(c_to_f, temperatures_c))
print("Celsius to Fahrenheit:", fahrenheit)

# Example 7: Filtering even numbers before mapping squares
numbers = [1, 2, 3, 4, 5, 6]
processed = list(map(lambda x: x**2, filter(lambda n: n % 2 == 0, numbers)))
print("Squared even numbers:", processed)
