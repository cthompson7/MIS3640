name = "jack"

print([ord(i) for i in name])
print([ord(ch.capitalize()) for ch in name])
print([ord(ch.capitalize()) for ch in name if ch not in "aeiou"])
print({ch:ord(ch.capitalize()) for ch in name if ch not in "aeiou"})

a = range(5)
print(type(a))

g = (x * x for x in range(5))

# next(g)
# next(g)
# next(g)
# next(g)

for i in g:
    print(i)

a = [True, False, False]
if any(a):
    print("yes")

if a[0] or a[1] or a[2]:
    print('yes')

print([letter == 's' for letter in 'babson'])
print(any(letter == 's' for letter in 'babson'))
print(all(letter == 's' for letter in 'babson'))

print(set(list('babson')))

b = set(list('babson'))
b.add("c")
print(b)

s1 = {1, 2, 3}
s2 = {2, 3, 4}

print(s1 & s2)

from collections import Counter
count = Counter('babson')
print(count)

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)

j = "jack"
first, *rest = j
print(first)
print(rest)
