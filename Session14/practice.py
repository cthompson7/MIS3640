t = ('a', 'b', 'c', 'd', 'e')

# t1 = 'a',
# print(type(t1))
#
# t = tuple('Babson')
#
# print(t)

print(t[0])
print(t[1:3])

t = ('A',) + t[1:]
# makes a new tuple and then makes t refer to it
print(t)

email = 'zli@babson.edu'
id, domain = email.split('@')
print(id)
print(domain)

t = divmod(7, 3)
print(t)

def printall(*args):
    print(args)

printall(1, 2.0, '3')
printall(1, 2.0, '3', None, True)

s = 'abc'
t = [0, 1, 2]
zip(s, t)

for pair in zip(s, t):
    print(pair)

list(zip(s, t))

def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False

for index, element in enumerate('abc'):
    print(index, element)

d = {'a':0, 'b':1, 'c':2}
t = d.items()
print(t)

import string
print(string.punctuation)




