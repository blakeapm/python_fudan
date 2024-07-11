#########################################################
#                                                       #
#                      Files                            #
#                                                       #
#########################################################

### Slide 6: Basic File Operations

# Open a file
file = open("example.txt", "w")
# Write to the file
file.write("Hello, World!\n")
# Close the file
file.close()

### Slide 7: Example of Opening and Closing a File

file = open("example.txt", "w")
file.write("Hello, World!\n")
file.close()

### Slide 8: Modes of Opening a File

# Open file to read
file = open("example.txt", "r")
# Read from file
content = file.read()
print(content)
# Close the file
file.close()

### Slide 9: Reading and Writing to Files

file = open("example.txt", "w")
file.write("Adding new content\n")
file.close()

### Slide 10: Check If a File Exists

import os.path
if os.path.isfile("example.txt"):
    print("File exists")
else:
    print("File does not exist")

### Slide 11: Using with and as for File Operations

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

#########################################################
#                                                       #
#       Exceptions and Exception Handling               #
#                                                       #
#########################################################

### Slide 13: Common Python Error Messages

# IndexError example
test = [1, 2, 3]
try:
    print(test[4])
except IndexError as e:
    print(e)

# In class example of failing silently

test = [1, 2, 3]
try:
    print(elephant)
except:
    pass

# In class example of actually handling exceptions

test = [1, 2, 3]
try:
    print(test[4])
except IndexError as e:
    last = len(test) - 1
    print(test[last])
    print("Out of bounds, printed last element, Error:", e)
except NameError:
    print("Encountered undefined variable. Error:", e)
    raise NameError("Need to define variable before accessing.")

# TypeError example
test = [1, 2, 3]
try:
    print(int(test))
except TypeError as e:
    print(e)

### Slide 14: More Common Python Error Messages

# NameError example
try:
    print(aardvark)
except NameError as e:
    print(e)

# More TypeError example
try:
    print('3'/4)
except TypeError as e:
    print(e)

### Slide 15: Syntax Error Example

# Missing close parenthesis
try:
    a = len([1, 2, 3]
    print(a)
except SyntaxError as e:
    print(e)

### Slide 16: Dealing with Exceptions

try:
    a = int(input("Tell me one number:"))
    b = int(input("Tell me another number:"))
    print(a/b)
except Exception as e:
    print("Bug in user input:", e)

### Slide 17: Handling Specific Exceptions

try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a/b = ", a/b)
    print("a+b = ", a+b)
except ValueError:
    print("Could not convert to a number.")
except ZeroDivisionError:
    print("Can't divide by zero")
except Exception:
    print("Something went very wrong.")

#########################################################
#                                                       #
#                  Virtual Environments                 #
#                                                       #
#########################################################

### Slide 22: Creating and Activating Virtual Environments

# Create a virtual environment
mkdir python-test
cd python-test
python -m venv myenv

# Activate the virtual environment
source ./myenv/bin/activate  # On Windows use `myenv\Scripts\activate`

### Slide 23: How to Deactivate a Virtual Environment

# Deactivate virtual environment
deactivate

#########################################################
#                                                       #
#                  Installing Packages                  #
#                                                       #
#########################################################

### Slide 31: Using pip to Install Modules

# Install a module using pip
pip install some_module_name

#########################################################
#                                                       #
#                  Introduction to Pandas               #
#                                                       #
#########################################################

### Slide 34: A Simple Demonstration

import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# Load dataset
penguins = pd.read_csv("penguins.csv")

# Filter data
species_data = penguins[penguins.species == "Adelie"]

# Create a scatter matrix
scatter_matrix(species_data)
plt.show()

### Slide 38: Creating a Series

import pandas as pd

# Create a Series
s = pd.Series(["a", "b", "c"])
print(s)

### Slide 39: Creating a Series

# Create a Series with an explicit index
s = pd.Series(["a", "b", "c"], index=[1, 2, 3])
print(s)

### Slide 40: Creating a Series with Dictionary

# Create a Series from a dictionary
s = pd.Series({"a": "A", "b": "B", "c": "C"})
print(s)

### Slide 41: Accessing Series

# Access elements in a Series
days = ["mon", "tue", "wed", "thu", "fri"]
sleephours = [6, 2, 8, 5, 9]
s = pd.Series(sleephours, index=days)
print(s["mon"])  # Output: 6
s["tue"] = 3
print(s[1])  # Output: 3

### Slide 42: Accessing Series

# Handle missing labels in a Series
print(s.get('sat', 'Label not found'))  # Using get with default value

### Slide 43: Slicing a Series

import pandas as pd

s = pd.Series(range(10))
print(s[1:3])  # Slicing by position
print(s[s > 5])  # Slicing by condition

### Slide 44: Head and Tail of a Series

import pandas as pd

s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(s.head(3))  # Display the first 3 elements
print(s.tail(3))  # Display the last 3 elements

### Slide 45: Subsetting by Numerical Index in Series

s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Access by index
print(s[[0, 2, 4, 6, 8]])  # Odd positioned elements

### Slide 46: Subsetting by Named Index in Series

s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
s.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(s[['a', 'c', 'e', 'g', 'i']])

### Slide 47: Operator Broadcasting in Series

import pandas as pd
s = pd.Series([1, 2, 3, 4])
print(s + 1)  # Increment each element by 1
print(s * 2)  # Double each element

### Slide 48: Handling Missing Values in Series

s = pd.Series([1, 2, None, 4])
print(s.fillna(0))  # Replace None with 0
print(s.dropna())  # Remove elements that are None

### Slide 49: Computing Statistics with Series

s = pd.Series([1, 2, 3, 4, 5])
print(s.sum())
print(s.mean())
print(s.median())
print(s.std())
print(s.prod())
print(s.max())
print(s.argmax())

### Slide 50: Summary Statistics in Series

s = pd.Series([1, 2, 3, 4, 5])
print(s.describe())  # Summary statistics
