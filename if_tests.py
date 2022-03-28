choice = 'sandwich'
foods = {'spam': 1.25, 'yogurt': 2.00, 'sandwich': 3.20, 'starvation': 0}
print(foods[choice])  # print as if it were a switch statement

print(foods.get('spam', 'That food doesn\'t exist!'))
print(foods.get('melon', 'That food doesn\'t exist!'))  # get 'melon', if that doesn't exist, return the right value
