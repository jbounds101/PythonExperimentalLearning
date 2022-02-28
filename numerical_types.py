# Chapter 5 Numerical Types
import decimal
import math
import random
from decimal import Decimal
#x = 9999999999999999999999999999999999999999999  # Python integers support infinite size in Python 3.#
#x = hex(x)  # A good way to translate am integer to hex
# can also translate to octal (oct) and binary (bin)
#print(x)
from fractions import Fraction

import fraction as fraction

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

# // floors after division, this can give weird results on negatives
print(5 // 2)
print(5 // -2)  # gives -3!!! 5/-2 = -2.5 rounded down = -3

# if you need to truncate as expected (div on negative)
print(math.trunc(5 / -2))

# unlimited number precision! 2 * 20000000000 is technically possible with enough memory

x = [1, 2, 3, 4, 5]
random.shuffle(x)
print(x)

print(0.1 + 0.1 + 0.1 - 0.3)  # gives a very close to zero approx
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.30'))  # Decimal constructor can be used to fix
# precision, will keep the highest precision decimal

decimal.getcontext().prec = 2  # can be used to globally set decimal precision (in the calling thread)
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.32341234132413420'))  # Decimal constructor can be
# used to fix

x = Fraction(1, 6)  # fraction type
print(x + 1)
x = Fraction('.12')  # can be created from floating point strings as well
print(x)
x = 1/3  # precision is as accurate as floating point hardware, can lose precision over many calculations
print(x)
# fraction and decimal both get rid of the precision issue at the cost of speed

x = 2.5.as_integer_ratio()
print(x)

x = Fraction(1, 2)
print(x + 1)  # fraction + int = fraction
print(x + 1.0)  # fraction + float = float




