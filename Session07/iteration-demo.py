# result = 0

# for i in range(10):
#     print("current number to be added ", i+1)
#     result = result + i + 1
#     print('new result after this iteration: ', result)

# print('The final result', result)

# for i in range(1, 11):
#     result = result + i

# print('The final result', result)

# for i in range(1,1001):
#     result = result + i

# print('The final result', result)

# for i in range(1,1001):
#     if i % 2 == 0:
#         result = result + i

# print('The final result', result)

# for i in range(1,1001, 2):
#         result = result + i
#
# print('The final result', result)

# factorialResult = 1

# for i in range(1,11):
#     factorialResult = factorialResult * i
#
# print('The final result is ', factorialResult)

# import time

# def countdown(n):
#     while n>0:
#         print(n)
#         time.sleep(1)
#         n = n-1
#     print('Blastoff!')

# countdown(10)

# counter = 0
# while counter < 10:
#     print("Here's Johnny!")
#     counter = counter + 1


# Exercise 3
# Copy the loop from above and encapsulate it in a function called mysqrt that takes a as a parameter, chooses a
# reasonable value of x, and returns an estimate of the square root of a.

# To test it, write a function named test_square_root that prints a table like this:

import math

def mysqrt(a):
    epsilon = 0.0000001
    x = 1
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return y

print(mysqrt(9))

def test_square_root():
    print("a   mysqrt(a)     math.sqrt(a)  diff")
    print("-   ---------     ------------  ----")

    for i in range(9):
        a = i+1
        b = mysqrt(a)
        c = math.sqrt(a)
        d = abs(b-c)
        print("{:.1f} {:.11f} {:.11f} {}".format(a, b, c, d))

test_square_root()
