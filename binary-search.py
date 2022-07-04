# Implementation of binary search
import random
import time

# Naive search scan entire list one item at a time
def naive_search(list, target):
    for index in range(len(list)):
        if list[index] == target:
            return index

    return -1

# Binary search uses divide and conquer
def binary_search(list, target, low = None, high = None):
    if low is None:
        low = 0

    if high is None:
        high = len(list) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if list[midpoint] == target:
        return midpoint
    elif target < list[midpoint]:
        return binary_search(list, target, low, midpoint - 1)
    else:
        return binary_search(list, target, midpoint + 1, high)

if __name__ == '__main__':
    length = 1000
    sorted_list = set()

    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))

    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search took ", (end - start)/length, " seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search took ", (end - start)/length, " seconds")
