# a = [1, 2, 3, 4]
#
# print(a[2])
# print(a[3])
# print(a[-1])
#
# b = ['spam', 2.0, 5, [10, 20]]
# print(b[3][0])
# print(b[0][2])
#
# AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
#
# AFC_east[3] = 'New York Giants'
#
# print(AFC_east)
#
# b[3][1] = 'Jack'
# print(b)



# Exercise #1
# What is the index of 'Apple'? 'Lisa'? 'On Rail'?

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[2][2])
print(L[1][2][1])


# for team in AFC_east:
#     print(team)
#
#
# numbers = [2, 0, 1, 6, 9]
#
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
#
# print(numbers)

# my_list = ['spam', 1, ['New England Patriots', \
#                        'Buffalo Bills', 'Miami Dolphins', \
#                        'New York Giants'], \
#            [1, 2, 3]]
# print(len(my_list))


# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)

# print([0] * 4)
# print(['Tom Brady', 'Bill Belichick']*3)

# t = ['a', 'b', 'c', 'd', 'e', 'f']
# print(t[1:3])
# print(t[0:4])
# print(t[-3:])
# print(t)

# t[1:3] = ['x', 'y']
# print(t)


# Exercise #2
# Read the documentation of the list methods at https://docs.python.org/3/tutorial/datastructures.html#more-on-lists.
# You might want to experiment with some of them to make sure you understand how they work. append, extend and sort
# are particularly useful.

t = ['a', 'b', 'c']
t.append(['d', 'e'])
print(t)

a = ['q', 'r', 's']
a.extend(['t', 'u', 'v'])
print(a)

vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort(reverse=False)
vowels.sort(reverse=True)
print(vowels)

group = ['e', 'e', 'a', 'u', 'e']
print(group.count('e'))

anotherlist = ['s', 'k', 'a', 'q', 'a']
anotherlist.remove('a')
print(anotherlist)
