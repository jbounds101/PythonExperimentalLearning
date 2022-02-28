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
