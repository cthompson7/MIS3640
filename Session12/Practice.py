# import turtle
#
# christian = turtle.Turtle()

# christian.fd(100)
# christian.lt(60)
# christian.fd(100)
# turtle.mainloop()

# def square(christian):
#     for i in range(4):
#         christian.fd(75)
#         christian.lt(150)
#         turtle.mainloop()

# def polygon(t, length, n):
#     for i in range(n):
#         t.fd(length)
#         t.lt(360/n)

# polygon(christian, 100, 5)

# christian.circle(120, 180)
# turtle.mainloop()

def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1)*n

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

team = 'New England Patriots'
letter = team[1] #The expression in brackets is called an index.
# print(letter)

# def histogram(s):
#     d = dict()
#     for c in s:
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c] += 1
#     return d

# h = histogram("Bookkeeper")
# print(h)
# numberOfE = h.get('e',0)
# print(numberOfE)


def histogram(s):
    d = dict()
    for c in s:
       d[c] = 1+d.get(c, 0)
    return d


def print_hist(h):
    for c in h:
        print(c, h[c])

# h = histogram('Massachusetts')
# print_hist(h)

# for key in sorted(h):
#     print(key, h[key])

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()

h = histogram('Massachusetts')
key = reverse_lookup(h, 2)
print(key)

t = ['a', 'b', 'c', 'd']
x = t.pop(1)
# pop modifies the list and returns
# the element that was removed.
print(x)
print(t)

# d.values()
# To find values in a dictionary


suspects = ['John', 'George', 'Ringo', 'Paul']
for name in suspects:
    if sum(["John"!=name, 'George'==name, 'Ringo'==name, "Ringo"!=name]) ==  3:
        print(name)
