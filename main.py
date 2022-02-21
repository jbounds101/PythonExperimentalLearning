import sys  # Load a library module
print(sys.executable)
print(2 ** 100)  # Raise 2 to a power
x = 'Spam!'
print(x[1])  # String repetition
print(x[1:3])  # Print chars 1 to 3 (not including 3)

#  x[1] = '3' Strings are immutable
x = x[:1] + '3' + x[2:]
print(x)

#  an easier way to remove or change a string[num] is this method with lists
s = list('strawberries')
s[:5] = ''
s = ''.join(s)  # make into a string (rather than a list)
print(s)

print(s.find('straw'))   # find returns the start index of a substring, or -1 if not find
print(s.find('ies'))

s = s.replace('rries', 'ars are scary')  # replace all occurrences of a pattern with another
s = s.capitalize()  # capitalize the first letter, make the rest lowercase
print(s)



