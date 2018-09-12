# a = int('42')
# type(a)
#
# int(3.99)
#
# int(-3.99)
#
# import math
# math.floor(3.99)
# math.floor(-3.99)
#
# float(3)
#
# float('3.14')
#
# str(3.14)
#
# age = input('Enter your name ')
#
# abs(100)
# abs(-100)
#
# max(1, 2, 3, 4, 5)


# def print_lyrics():
#     print("Hey Jude. Don't make it bad.")
#     print("Take a sade song and make it better.")

# print_lyrics()
#
# print(type(print_lyrics()))

# def repeat_lyrics():
#     print_lyrics()
#     print('Na- na - na - na - na - na - na - na - na - na - na!')
#     print_lyrics()

# repeat_lyrics()

# def print_twice(name):
#     print('first time:')
#     print(name)
#     print('the second time:')
#     print(name)

# print_twice('Matthew')

# name = input('Please enter your name: ')

# print_twice(name)

# def my_abs(n):
#     if n < 0:
#         return(-n)
#     else:
#         return(n)

# print(my_abs(100))
# print(my_abs(-4))

# def give_a_break():
#     return 'break'

# print(give_a_break())

# def give_me_another_break():
#     str1 = 'break'
#     print('another break')
#     return str1

# print(give_me_another_break())

# result = print_twice("Bing")
# print(result)

# Exercise 1 Session 4: Define a Function Quadratic to Solve a Quadratic Equation

import math

ca = float(input("Please input the coefficient of a: "))
cb = float(input("Please input the coefficient of b: "))
cc = float(input("Please input the coefficient of c: "))

def quadratic(a, b, c):
    d = b**2-4*a*c

    if d < 0:
        print("This problem has no real solution.")
    elif d == 0:
        oneSol = (-b-math.sqrt(d))/(2*a)
        print("This problem has only one solution: "+(str(oneSol))+".")
    else:
        sol1 = (-b-math.sqrt(d))/(2*a)
        sol2 = (-b+math.sqrt(d))/(2*a)
        print("This problem has two solutions: {0}, {1}.".format(str(sol1),str(sol2)))

quadratic(ca,cb,cc)
