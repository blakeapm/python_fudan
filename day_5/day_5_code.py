#########################################################
#                                                       #
#                Conditional Statements                 #
#                                                       #
#########################################################

### Slide 3: Equality vs. Assignment Operators

x = 10 # Assigns value of 10 to 'x'
x == 10 # Checks equality of 'x' and 10
x == 5 # Checks equality of 'x' and 5
x = 5 # Assigns value of 5 to 'x'
x == 5 # Checks equality of 'x' and 5

### Slide 4: Boolean Expressions

1 > 2
"apple" != "banana"
5 == 5
10 <= 10

### Slide 5: Logic Operators

a = True
b = False
a and b
a or b
a and not b
b and not a
a or not b
b or not a

### Slide 6: Equality vs. Identity

a = [1, 2, 3]
b = [1, 2, 3]
c = a
a == b # Same value, different object
a is b # Not the same object
a is c # 'c' and 'a' refer to the same object

### Slide 7: Combining Boolean Expressions and Logical Operators

x = 15
y = 10
print(x > 10 and y < 15)
if x > 10 and y < 15:
    print("Both conditions met.")
else:
    print("Conditions not met.")

### Slide 8: if Statements

x = 42
if x > 0:
    print('x is positive')

### Slide 9: else Statements

x = -42
if x > 0:
    print('x is positive')
else:
    print('x is not positive')

### Slide 10: elif Statements

x = 0
if x > 0:
    print('x is positive')
elif x < 0:
    print('x is negative')
else:
    print('x is zero')

### Slide 11: Nested Conditionals

x = 42
y = 3
if x == 42:
    if y == 3:
        print('x is 42 and y is 3')

#########################################################
#                                                       #
#                        Iteration                      #
#                                                       #
#########################################################

### Slide 12: range() Function

for i in range(5, 15, 5):
    print(i)

### Slide 13: for Loops

for i in range(10):
    if i % 2 == 0:
        print(i)

### Slide 14: while Loops

i = 5
while i > 0:
    print(i)
    i -= 1
print('Blastoff!')

### Slide 15: The break Statement

count = 0
for i in range(100):
    count += 1
    if i == 10:
        break
print(count)

### Slide 16: The continue Statement

count = 0
for i in range(10):
    if i % 2 == 0:
        continue
    count += 1
print(count)

#########################################################
#                                                       #
#                 Working with Strings                  #
#                                                       #
#########################################################

### Slide 17: A String is a Sequence

fruit = 'banana'
letter = fruit[1]
print(letter)

### Slide 19: String Indexing Example

s = "abc"
s[0]
s[1]
s[3]
s[-1]
s[-2]

### Slide 21: String Slicing Example

s = 'Monty Python'
s[0:5]
s[6:12]
s[::2]
s[6:12:3]
s[:: -1]

### Slide 22: Strings are Immutable

s = "hello"
s[0] = 'y'
s = 'y' + s[1:len(s)]

### Slide 23: Length of Strings: len()

fruit = 'banana'
length = len(fruit)
print(length)

### Slide 24: Traversal with a for Loop

fruit = 'banana'
for char in fruit:
    print(char)

### Slide 26: String Methods: Capitalization

program = 'lse -fudan summer school'
program.lower()
program.upper()
program.title()

### Slide 27: String Methods: Stripping Whitespace

program = ' lse -fudan summer school'
program.strip()
program.rstrip()
program.lstrip()

### Slide 28: String Methods: Finding and Replacing

program = 'lse -fudan summer school'
program.startswith('lse')
program.endswith('ool')
program.count('summer')
program.replace('summer school', 'conference')
program.find('fudan')

### Slide 30: String Comparison

word = 'banana'
if word == 'banana':
    print('All right, bananas.')
