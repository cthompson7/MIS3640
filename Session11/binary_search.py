def binary_search(my_list, x):
    '''
    this function adopts bisection/binary search to find the index of a given
    number in an ordered list
    my_list: an ordered list of numbers from smallest to largest
    x: a number
    returns the index of x if x is in my_list, None if not.
    '''
    left = 0
    right = len(my_list)-1
    middle = int((left+right)/2)

    if x not in my_list:
        return None

    while (right - left > 1):
        if my_list[middle] == x:
            return middle
        elif my_list[middle] > x:
            right = middle
            middle = int((left+right/2))
        elif my_list[middle] < x:
            left = middle
            middle = int((left+right/2))

    if my_list[right] == x:
        return right
    elif my_list[left] == x:
        return left

test_list = [1, 3, 5, 235425423, 23, 6, 0, -23, 6434]
test_list.sort()

print(binary_search(test_list, -23))
print(binary_search(test_list, 0))
print(binary_search(test_list, 235425423))
print(binary_search(test_list, 30))

# expected output
# 0
# 1
# 8
# None
