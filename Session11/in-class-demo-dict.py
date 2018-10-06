# team = 'Patriots'
# t = list(team)
#
# "".join(t)
# " ".join(t)
# ".".join(t)
#
# list(team)
#
# len(team)
#
# t = list(team)
#
# len(t)
#
# len(team.split())
#
# team.split()
#
# url = 'www.bbc.co.uk'
# url.split('.')[1]
#
# url_splitted = url.split(".")
# print(url_splitted)
# ".".join(url_splitted)
#
# t = sorted(t)
#
# t + [4]
#
# x = [1, 2, 3, 4]
# x.extend([5])
# print(x)
#
# y = [2, 3, 1]
#
# t = ['New', 'England', 'Patriots']
# team = '!!'.join(t)
# print(team)
#
# a = 'banana'
# b = 'banana'
# print(a is b)


# Dictionary Handout
# grades = dict()
# print(grades)
#
# grades['Defne'] = 90
# print(grades)
#
# grades ={'Defne': 90, 'Jack': 75, 'Angela': 85}
# print(grades)
#
# print(grades['Jack'])
#
# print(len(grades))
#
# print('Jack' in grades)
#
# print(90 in grades.values())


# Exercise #1
# Rewrite function histrogram using get. You should be able to eliminate the if statement.

# def histogram(s):
#     d = dict()
#     for c in s:
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c] += 1
#     return d

def histogram(s):
    d = dict()
    for c in s:
       d[c] = 1+ d.get(c, 0)
    return d

# print(histogram("Bookkeeper"))


# Exercise #3
# numbFibCalls is another global variable utilized in the function. This global variable is utilized to count the
# number of times that the function is called in both fib(n) and fib_efficient(n). numbFibCalls is set to zero in both
# functions, but when each function runs, returns different values to be printed. This is much different than the usage
# case of the other global variable, known.


# Exercise #4
# 1.) Write a function that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter
# what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

w = open('words.txt')

def store_words():
    dict_words = dict()
    for line in w:
        word = line.strip()
        dict_words[word] = word

    return dict_words

# print(store_words())

# 2.) Write a function named has_duplicates that takes a list as a parameter and returns True if there is any object
# that appears more than once in the list.

myList = [5, 4, 4, 3, 1, 2]

def has_duplicates(theList):
    myDictionary = dict()
    for value in theList:
        myDictionary[value] = 1 + myDictionary.get(value, 0)
        if myDictionary[value] > 1:
            return True

    return False

# print(has_duplicates(myList))
