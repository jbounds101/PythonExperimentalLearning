# Variables in Python are all pointers (references) to objects!

a = 5
b = 5
# a and b both point to the same object, however, they will not after a change to one of the vars
a += 1
# a -> 6
# b -> 5

wack = [1, 2, 3]  # this isn't the case for mutable objects though
lack = wack  # these now point to the same object, which is mutable and therefore is changed for both vars
if lack is wack:  # 'is' checks for an identical reference object (for example, using == could check for same value but
    # 'is' checks for the object id to be the exact same

    # !!!!!!! 'is' compares pointers
    print('true')
lack[0] = 40
print(wack)

lack = list.copy(wack)  # this would be the proper way to copy the list
lack = wack[:]  # this is also an effective way to do this!

if lack is wack:
    print('true')
else:
    print('false')  # notice how, since the two lists are not the same reference list, they 'is' not the same
