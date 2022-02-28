# Section: Files
f = open('data.txt', 'w')  # create a data.txt file with write privileges
f.write('Hello\n')
print(f.write('world!\n'))  # returns the number of characters printed
f.close()

f = open('data.txt')  # reading is the default operation
text = f.read()  # files are always read as strings
print(text)
f.close()

# Section: Sets
x = set('spam')  # sets are immutable, unordered collections of unique objects
# x = set('s', 'p', 'a', 'm') is the same set
y = set('ham')
print(x, y)
print(x & y)  # union of x and y
print(x | y)  # intersection of x and y
print(x - y)  # difference of x and y
print(x > y)  # check if x is a superset of y
print(x == y)  # checks if they are equal, regardless of order