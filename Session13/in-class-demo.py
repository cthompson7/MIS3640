# bytes is the basic storage datatype for python
# Use bytes for multi-language data

# class_roster = ['Jonathan Beltran', 'Waylon Ryan', 'Kyle Lawson']
# a = class_roster[1:]

# a, *b = class_roster
# *a, b = class_roster
# a, *b, c = class_roster

# Set: list, but no duplicate items allowed.
# a = [1, 2, 3, 1, 4]
# print(set(a))

# When we print it, what it looks like
# a = "\nn"
# print(repr(a))

# 63 = 16 * 3 + 15
# 64 = 16*4 + 0
# ff = 16 * 15 + 15 = 255
# RGB(255, 255, 255) = white

# def a(b):
#     # if b > 10:
#     #     return True
#     # else:
#     #     return False
#
#     return b > 10

# print(a(11))

# enumerate ***
# def enumeratePractice():
#     for i, name in enumerate(class_roster):
#         print(i, name)

# enumeratePractice()

# Module external python file/package

# roster = {}
#
# def newRoster():
#     for name in class_roster:
#         roster[name] = 0

# roster = {name: 0 for name in class_roster}
#
# print(roster)

# list is square brackets
# dictionary is squiggly brackets

# roster = [len(name) for name in class_roster]
# print(roster)

# import random
#
# class_roster = {'Jonathan Beltran': 0, 'Allison Fernandez': 1, 'Siddhanth Goyal': 0, 'Jingyu He': 0, 'Defne Ikiz': 0, 'Zirui Jiao': 0, 'Pranjal Joshi': 0, 'Dong Hyun Kim': 0, 'Ha Min Ko': 0, 'Kyle Lawson': 0, 'Christine Lee': 1, 'Connie Li': 1,
#                 'Qinyi Li': 0, 'Matthew Michalke': 0, 'Ho Wang Alastair Ng': 1, 'Jonghyun Park': 0, 'Alden Pexton': 2, 'Shriya Rathi': 2, 'Waylon Ryan': 1, 'Christian Thompson': 3, 'Angela Tsung': 2, 'Aaron Wendell': 0, 'Sarah Zazyczny': 0, 'Shiyue (Shirley) Zong': 0}
#
# min_times = min(class_roster.values())
# pool = []
#
# for name in class_roster:
#     if class_roster[name] == min_times:
#         pool.append(name)

# random_name = random.choice(pool)

# class_roster[random_name] += 1

# print(class_roster)

# for name, times in class_roster.items():
#     print('name', name, 'times:', times, sep ="_____")
#
# names = sorted(class_roster)
# import random
# grades = [random.randint(60, 99) for i in range(len(names))]


# Generic Operations on Containers
t = ('dog, job, steve, jack, george, solo cup, backpack')
a = "This is a long sentence that will be utilized to perform operations on."
list1 = [456, 700, 200], [123, 'xyz', 'zara', 'abc']
list2 = [55, 333, 21]

print(len(a))
print(min(list1))
print(max(list1))
print(sorted(list1))
print("dog" in t)

for letter in enumerate(t):
    print(letter)

print(zip(list1, list2))

def all(list1):
    for element in list1:
        if not element:
            return False
    return True

print(all(list1))

def any(list2):
    for element in list2:
        if element:
            return True
    return False

print(any(list2))

print(reversed(t))
print(t.index(5))

print(t.copy(0))
print(t.deepcopy(0))

list2.append(45)
list1.extend("Hello")
list2.insert(1, "Goodbye")
list1.remove("Hello")
list2.pop("Goodbye")
list2.sort()
