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
