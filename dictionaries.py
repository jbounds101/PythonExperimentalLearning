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