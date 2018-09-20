# 3.) The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,
#
# gcd(2, 12) = 2
#
# gcd(6, 12) = 6
#
# gcd(9, 12) = 3
#
# gcd(17, 12) = 1
#
# See this website for an example of Euclid's algorithm being used to find the gcd. https://en.wikipedia.org/wiki/Euclidean_algorithm#Worked_example
#
# Write a program, greatest_common_divisor.py to implement this idea recursively. The function gcd() takes in two positive integers and returns one integer.


# int1 = int(input('Please enter your first integer: '))
# int2 = int(input('Please enter your second integer: '))

def gcd(int1, int2):
    if int2 > int1:
        return gcd(int2, int1)

    if int1 % int2 == 0:
        return int2

    return gcd(int2, int1 % int2)

# print(gcd(int1,int2))

# 4.) Implement algorithm for tower of Hanoi. https://www.mathsisfun.com/games/towerofhanoi.html

def move(n, source, bridge, destination):
    if n==1:
        print(source+" --> "+destination)
        return

    move(n-1, source, destination, bridge)
    print(source+" --> "+destination)
    move(n-1, bridge, source, destination)

# move(3, 'A', 'B', 'C')
