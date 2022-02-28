# Section: Tuples
t = (1, 2, 3, 4)  # tuples are immutable like strings
t += (5, 6)  # this makes a new object
print(t)

t = (1,)  # one item tuples require a comma to create
t = (2,) + t
print(t)

# tuples are not used nearly as often as lists, however, they are useful because of their immutability
