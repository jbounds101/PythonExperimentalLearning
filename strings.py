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

# Part 2

print(r'C:\myhomedirectory!')  # r'string' allows for literal strings (no need to escape any characters)

spanning = """
always
    look
        on the
            bright side"""
# multiline strings can be created with triple quotes, these keep spacing from the left!

print(spanning)

word = 'king'
print(word[::-1])  # reverses a string
# the [#:#:n] subset n value refers to the step of the subset, for example, the default is 1, which steps up one index
# until at the end-1, a step of 2 steps up two indices, and -1 goes backwards

print('%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'})  # formatting on dictionaries

spammer = {'food': 'spam', 'quantity': 100}
print('{quantity}! That\'s a lot of {food}'.format(**spammer))  # formatting on dictionary object
# ** is used to 'unpack' a dictionary

reply = """
Greetings...
Hello {name}!
Your age is {age}
"""
name = 'Bob'
age = '16'
print(reply.format(**vars()))  # a way to extract non object variables into strings
