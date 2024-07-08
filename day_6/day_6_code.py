#########################################################
#                                                       #
#                  Regular Expressions                  #
#                                                       #
#########################################################

### Slide 2: Searching with re.search

import re
search = re.search(r'[A-Za-z]+\-[A-Za-z]+', 'LSE -Fudan Summer School')
print(search)
print(search.start())
print(search.end())
print(search.group())

### Slide 3: Using re.sub for Substitutions

import re
result = re.sub(r'[A-Za-z]+\-[A-Za-z]+', 'Day 5 of', 'LSE -Fudan Summer School')
print(result)
result = re.sub(r'([A-Z]+|[0-9]+)', '***', 'ABC abc 123')
print(result)

#########################################################
#                                                       #
#                       Recursion                       #
#                                                       #
#########################################################

### Slide 6: Recursion

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

countdown(3)

### Slide 7: Recursion Example

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

### Slide 8: Checking Types

def factorial(n):
    if not isinstance(n, int) or n < 0:
        print("Invalid input.")
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial("fred"))

#########################################################
#                                                       #
#                         Lists                         #
#                                                       #
#########################################################

### Slide 10: Lists are Mutable

profs = ['Meng', 'Hildebrandt', 'Ding', 'Miller', 'Puppim de Oliveira', 'Mendez', 'Alden']
print(profs)

### Slide 11: Traversing a List

numbers = [17, 123]
numbers[1] = 5
print(numbers)

### Slide 12: Traversing a List

for prof in profs:
    print("Dr.", prof)

### Slide 13: List Operations

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

### Slide 14: List Slices

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)

### Slide 15: List Methods

t = ['a', 'b', 'c']
t.append('d')
print(t)
t.extend(['e', 'g', 'f'])
print(t)
t.sort()
print(t)

### Slide 16: Deleting Elements (pop)

t = ['a', 'b', 'c', 'd']
x = t.pop(1)
print(t)
print(x)

### Slide 17: Deleting Elements (remove)

t = ['a', 'b', 'c', 'b']
t.remove('b')
print(t)

### Slide 18: Deleting Elements (del)

t = ['a', 'b', 'c', 'd']
del t[1]
print(t)

#########################################################
#                                                       #
#                     Dictionaries                      #
#                                                       #
#########################################################

### Slide 19: A Dictionary is a Mapping

class_teachers = {
    'Hildebrandt': 'Social Governance and Policy Innovation',
    'Meng': 'Chinese Media, Global Contexts',
    'Miller': 'Python Data Collection and Management'
}
print(class_teachers['Miller'])

### Slide 20: Dictionary Operations

class_teachers['Ding'] = 'Comparative Public Policy'
class_teachers['Miller'] = 'Python for Public Policy Research'
print(class_teachers)

### Slide 21: Dictionary as a Set of Counters

def histogram(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1
    return d

h = histogram('brontosaurus')
print(h)

### Slide 22: Looping and Dictionaries

student_count = {'Miller': 10, 'Hildebrandt': 15, 'Ding': 10}
for prof in student_count:
    print(prof, student_count[prof])

### Slide 23: Reverse Lookup

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError('Value does not appear in the dictionary')

h = histogram('brontosaurus')
try:
    print(reverse_lookup(h, 2))
except ValueError as e:
    print(e)

### Slide 24: Dictionaries and Lists

d = {'a': [1, 2, 3], 'b': [4, 5, 6]}
d['a'].append(4)
print(d)

#########################################################
#                                                       #
#                        Tuples                         #
#                                                       #
#########################################################

### Slide 25: Tuples are Immutable

t = ('a', 'b', 'c', 'd', 'e')
try:
    t[0] = 'A'
except TypeError as e:
    print(e)

### Slide 26: Tuple Assignment

a, b = 1, 2
print(a)
print(b)

### Slide 27: Tuples as Return Values

def minutes_to_hours(minutes):
    hours = minutes // 60
    remainder = minutes - hours * 60
    return (hours, remainder)

hours, minutes = minutes_to_hours(185)
print(hours, "hours", minutes, "minutes")

### Slide 28: Variable-length Argument Tuples

def printall(*args):
    print(args)

printall(1, 2.0, '3')

### Slide 29: Lists and Tuples

s = 'abc'
t = [0, 1, 2]
zipped = list(zip(s, t))
print(zipped)

### Slide 30: Iterating through Lists of Tuples

t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
    print(letter, number)
    
#########################################################
#                                                       #
#          List and Dictionary Comprehensions           #
#                                                       #
#########################################################

### Slide 31: List Comprehensions

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)

### Slide 32: More List Comprehensions

names = ['Yuki', 'Jorge', 'Mei', 'Aya']
lengths = [len(name) for name in names]
print(lengths)

### Slide 33: Dictionary Comprehensions

names = ['Yuki', 'Jorge', 'Mei', 'Aya']
name_lengths = {name: len(name) for name in names}
print(name_lengths)

### Slide 34: Using Conditionals in List Comprehensions

ages = [22, 35, 27, 21, 40]
adults = [age for age in ages if age >= 21]
print(adults)

### Slide 35: Dictionary Comprehensions with Conditionals

ages = {'Yuki': 22, 'Jorge': 17, 'Mei': 25, 'Aya': 21}
adults_dict = {name: age for name, age in ages.items() if age >= 21}
print(adults_dict)

### Slide 36: Nested List Comprehensions

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)
