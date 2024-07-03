#########################################################
#                                                       #
#  Objects, Types, Variables, Expressions and Commands  #
#                                                       #
#########################################################

### Slide 11: The Python Shell

print("Hello, World!")

### Slide 10: Types

type("Fudan University")
type(1)
type(True)
type(1.5)

### Slide 11: Type Conversions (Casting)

float(1)
bool(1)
int(1.5)
str(1.5)

### Slide 14: Order of Operations

2 + 3 * 4 ** 2
(2 + 3) * 4 ** 2
2 + (3 * 4) ** 2

### Slide 15: String Operations

first = 'throat'
second = 'warbler'
first + second
'Spam'*3

### Slide 16: Comments

# print("This will not print")
print("This will print")

# Calculate the percentage of the amount
amount = 120
discount_percentage = 10

# Calculate discount amount
discount_amount = (discount_percentage / 100) * amount

# Print the final price
print(amount - discount_amount)

### Slide 18: Types of Errors: Syntactic Error

print(Fudan University)

### Slide 19: Types of Errors: Static Semantic Error

"number: " + 5

### Slide 20: Types of Errors: Semantic Error

"1" + "1"

### Slide 21: Variables and Assignment

message = 'And now for something completely different'
n = 17
pi = 3.1415926535897931

### Slide 22: Why Variables?

pi = 3.14
radius = 10
circumference = pi * (2 * radius)
area = pi * (radius ** 2)

### Slide 23: Reassignment Example

pi = 3.14
radius = 2.2
area = pi * (radius ** 2)
print(area)
radius = radius + 1  # radius is now 3.2
print(area)
area = pi * (radius ** 2)
print(area)

### Slide 24: Floor Division and Modulus

minutes = 105
hours = minutes // 60
remainder = minutes - hours * 60
print(hours, "hour", remainder, "minutes")

#########################################################
#                                                       #
#                      Functions                        #
#                                                       #
#########################################################

### Slide 25: What is a Function?

def is_even(i):
    return i % 2 == 0

is_even(3)  # Calls the function with 3 as an argument

### Slide 26: Another Function Example

def minutes_to_hours(minutes):
    hours = minutes // 60
    remainder = minutes - hours * 60
    print(hours, "hour", remainder, "minutes")
    return hours, remainder

hours, minutes = minutes_to_hours(105)
print(hours)
print(minutes)
hours, minutes = minutes_to_hours(268)

### Slide 29: Defining Functions

def say_hello(name):
    print("Hello", name)

say_hello("Dr. Miller")

### Slide 30: Defining Functions

def say_hello(name, question=", how are you?"):
    print("Hello", name, question)

say_hello("Dr. Miller")
say_hello("Dr. Miller", question=", you alright?")

### Slide 31: Parameters and Arguments

def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice('Spam')

### Slide 33: Practical Example: Function Scope

def f(x):
    x = x + 1  # Local modification of x
    print(x)  # Displays the local value of x
    return x  # Returns the modified x

x = 3  # Global x
z = f(x)  # Calls f with global x, returns new value to z

### Slide 36: Fruitful Functions and Void Functions

def print_hello():
    print("Hello")  # Void function

def sum_two_numbers(a, b):
    return a + b  # Fruitful function

a = print_hello()
print(a)
b = sum_two_numbers(5, 3)
print(b)