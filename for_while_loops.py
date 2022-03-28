for i in range(5):
    print(i)
else:
    # you can use else on loops to check if a loop exited 'normally', without break
    print('loop exited normally!')


def func():
    pass  # can't leave a function blank, an example of using pass (which does nothing essentially)


foods = {'spam': 1.25, 'yogurt': 2.00, 'sandwich': 3.20, 'starvation': 0}
for x in foods:
    print(x, end=' ')  # gets the key
print()

T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:
    print(a, b)  # can iterate over pairs

for both in T:
    a = both  # this gets the pair
    print(a)

for both in T:
    a, b = both  # this separates the pair
    print(a, b)
