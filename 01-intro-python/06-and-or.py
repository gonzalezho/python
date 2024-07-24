# The Complete Python Course: https://go.tecla.do/cpc
# Lecture: The 'and' & 'or' keywords in Python
# E-book: https://complete-python.teclado.com/intro/lectures/and_or/

age = 25  # could be int(input("Enter your age: "))

result = age > 18 and age < 65  # True and True
print(result)  # True

# --

age = 25

result = age < 18 and age > 65  # False and False
print(result)  # False

# --

age = 25

result = age < 18 and age < 65  # False and True
print(result)  # False

# --

age = 25

result = age < 18 and age < 65  # False and ??? doesn't matter
print(result)  # False

# --

age = 25

result = age > 18 or age < 65  # True and ??? doesn't matter
print(result)  # True

# --

bool(0)  # False, zero
bool(13)  # True

bool("")  # False, empty string
bool("Hello")  # True

bool([])  # False, empty list
bool([1, 3, 5])  # True

# --

default_age = 30
age = 0

user_age = age or default_age
print(user_age)  # 30

# --

default_greeting = "there"
name = input("Enter your name: (optional) ")

user_name = name or default_greeting

print(f"Hello, {user_name}!")

# --

# Read more and take the quiz in the e-book!
# https://complete-python.teclado.com/intro/lectures/and_or/
