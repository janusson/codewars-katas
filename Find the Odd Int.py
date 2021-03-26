# Find the Odd Int.py
"""
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
"""

# Sample data
sequence = [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]
sequence2 = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]
sequence3 = [20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]


def find_it(seq):
    # return the integer(s) in a list if they occur an odd number of times.
    # for this problem, return any item in that list
    return [i for i in seq if seq.count(i) % 2][0]


find_it(sequence2)
