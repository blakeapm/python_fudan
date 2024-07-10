t = ('a', 'b', 'c', 'd', 'e')
try:
    t[0] = 'A'
except TypeError as e:
    print(e)

print("This line is executed in the script.")