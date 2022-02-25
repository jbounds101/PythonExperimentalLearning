import sys  # Load a library module

print(sys.executable)
print(2 ** 100)  # Raise 2 to a power

# Section: String Formatting
x = 'Spam!'
print(x[1])  # String repetition
print(x[1:3])  # Print chars 1 to 3 (not including 3)

#  x[1] = '3' Strings are immutable, not possible (calls error)
x = x[:1] + '3' + x[2:]
print(x)

#  an easier way to remove or change a string[num] is this method with lists
s = list('strawberries')
s[:5] = ''
s = ''.join(s)  # make into a string (rather than a list)
print(s)

print(s.find('straw'))  # find returns the start index of a substring, or -1 if not find
print(s.find('ies'))

s = s.replace('rries', 'ars are scary       ')  # replace all occurrences of a pattern with another
s = s.capitalize()  # capitalize the first letter, make the rest lowercase
print(s)

s = (s.rstrip()).split(' ')  # split into list using a delimiter after stripping the whitespace from the right
print(s)

s = '%s, eggs, %s' % ('bacon', 'eggs')  # a way to format strings
print(s)
s = '{0}, cars, {1}'.format('planes', 'trucks')  # a more legible way
print(s)
s = '{}, cars, {}'.format('planes', 'trucks')  # can also exclude numbers
print(s)

# Section: Dictionaries

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}  # a dictionary, has a "key" and a "value"
D['quantity'] += 1;  # dictionaries are mutable
print(D)

D = {}  # dictionaries can also be changed/created on the fly
D['name'] = 'Joe'  # assign key 'name' to 'joe'
D['occupation'] = 'Day-trading'
D['money'] = -1000000
print(D)

person = dict(name='joe', job='programmer', salary='999999999')  # another way to make a dictionary
personTwo = dict(zip(['name', 'job', 'salary'], ['joe', 'programmer', '999999999']))  # zipping to make a dictionary

# Dictionary mappings are not positional, so they may not print out in the same order!

# Section: Tuples
t = (1, 2, 3, 4)  # tuples are immutable like strings
t += (5, 6)  # this makes a new object
print(t)

t = (1,)  # one item tuples require a comma to create
t = (2,) + t
print(t)

# tuples are not used nearly as often as lists, however, they are useful because of their immutability

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

# Chapter 5 Numerical Types
#x = 9999999999999999999999999999999999999999999  # Python integers support infinite size in Python 3.#
#x = hex(x)  # A good way to translate am integer to hex
# can also translate to octal (oct) and binary (bin)
#print(x)
x = 99.6
#x = x.as_integer_ratio()  # converts a float to a ratio of integer (can get pretty massive)
# commented out since it was eating my memory
print(x)
print(x / 1)   # true division, will convert as needed in Python 3.# (doesn't happen in 2 versions)
print(x // 1)  # integer division, gets rid of remainder (same as div)

x = 1
y = 2
z = 3

if x < y < z:  # can chain comparisons, this is equal to (x < y and y < z)
    print('true')
if x < y and y < z:
    print('see, it\'s the same!')

x = 10
y = 1.2
print(x + y, x - y)  # this technically creates a tuple
x = x + y  # integer 10 is 'ranked up' and the two floats are added (result is now a float)
print(x)


x = 'king'
y = 'kong'
print(x + y)  # polymorphism, strings + is different from numerical




