"""
Question 1:
If the number, n, is divisible by 4, return True; return False otherwise. Return False if n is divisible by 100 (for example, 1900); the only exception is when n is divisible by 400(for example, 2000), return True.
"""


def is_special(n):
    if n % 400 == 0:
        return True
    elif n % 100 == 0:
        return False
    elif n % 4 == 0:
        return True
    else:
        return False

# When you've completed your function, uncomment the
# following lines and run this file to test!


# print(is_special(2020))
# print(is_special(300))
# print(is_special(2018))
# print(is_special(2000))


"""
-----------------------------------------------------------------------
Question 2:
"""


def detect(a, b, n):
    if a == n or b == n:
        return True
    elif a + b == n:
        return True
    elif a*b == n:
        return True
    elif a - b == n or b - a == n:
        return True
    else:
        return False
    """
    Returns True if either a or b is n, or if the sum or difference or product of a and b is n.
    """


# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(detect(2018, 9, 2018))
# print(detect(2017, 1, 2018))
# print(detect(1009, 2, 2018))
# print(detect(2020, 2, 2018))
# print(detect(2017, 3, 2018))

"""
-----------------------------------------------------------------------
Question 3:
Write a function with loops that computes the sum of all cubes of all the odd numbers between 1(inclusive) and n (inclusive if n is not even).
"""


def sum_cubes_of_odd_numbers(n):
    s = 1
    sumOfCubes = 0
    while s <= n:
        if n == 1:
            return 1
        if s % n != 0:
            sumOfCubes = sumOfCubes + s**3
            s = s + 2
            if s == n:
                sumOfCubes = sumOfCubes + s**3
                return sumOfCubes
    return sumOfCubes

# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(sum_cubes_of_odd_numbers(1))
# print(sum_cubes_of_odd_numbers(10))
# © 2018 GitHub, Inc.
