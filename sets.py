# Section: Sets
x = set('spam')  # sets are immutable (and contain only immutable objects), unordered collections of unique objects
# x = set('s', 'p', 'a', 'm') is the same set
y = set('ham')
print(x, y)
print(x & y)  # union of x and y
print(x | y)  # intersection of x and y
print(x - y)  # difference of x and y
print(x > y)  # check if x is a superset of y
print(x == y)  # checks if they are equal, regardless of order

x = {1, 2, 3, 4}  # this also creates sets
print(x)
