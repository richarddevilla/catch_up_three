import sys


def recursive_min(nested_list):
    """
    the function takes a list of integers or another list of integers
    it then check the list and return the smallest integer
    :param nested_list:
    :return:
    """
    low_number = 99
    for item in nested_list:
        if not isinstance(item, list):
            if low_number > item:
                low_number = item
        else:
            if low_number > recursive_min(item):
                low_number = recursive_min(item)
    return low_number


def count_occurrences(nested_list, number):
    """
    takes an integer and list of integer or another list of integers as parameter
    then look for how many times a number appeared in the list
    :param nested_list:
    :param number:
    :return:
    """
    occurrences = 0
    for item in nested_list:
        if not isinstance(item, list):
            if number == item:
                occurrences += 1
        else:
            occurrences += count_occurrences(item, number)
    return occurrences


flattened_list = []


def flatten(nested_list):
    """
    takes an integer and list of integer or another list of integers as parameter
    and append all item into a single list
    :param nested_list:
    :return:
    """
    for item in nested_list:
        if isinstance(item, int):
            flattened_list.append(item)
        else:
            flatten(item)
    return flattened_list


def test_limit(x=1):
    """
    function would print count until recursion limit is reached
    :param x:
    :return:
    """
    x+=1
    print(x)
    test_limit(x)

#1A
nested_list = [2, 3, 4, [4, 5, 6, [8, 9, 10, [11, 12, 13], 14], 15, 16], 17]
print(recursive_min(nested_list))
#1B
number = int(input('Please input a number to check for occurrence in the nested list: '))
print(count_occurrences(nested_list, number))
#1C
print(flatten(nested_list))

#2A
print(sys.getrecursionlimit())
input('Press any key to start recursion limit test 1')
try:
    test_limit()
except Exception as e:
    print(e)
#2B
input('Press any key to start recursion test 2 with reduced limit')
sys.setrecursionlimit(500)
try:
    test_limit()
except Exception as e:
    print(e)

