# Sum of two lowest positive integers.py
"""
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers.
No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
[10, 343445353, 3453445, 3453545353453] should return 3453455.

ARRAYS

"""
arr = [19, 5, 42, 2, 77]


def sum_two_smallest_numbers(numbers):
    if len(arr) > 4:
        arr.sort()
        lowSum = arr[0] + arr[1]
        return lowSum


sum_two_smallest_numbers(arr)
