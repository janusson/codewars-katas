"""
Testing 1-2-3.py
#!%%python3
Your team is writing a fancy new text editor and you've been tasked with
implementing the line numbering.

Write a function which takes a list of strings
and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string.
Notice the colon and space in between.
"""


def testing123(s):

    for i in range(len(s)):
        ln = f"{i}: "
        line = s[i]

    return print('testing123 complete!')


strang = ['a', 'b', 'c']
# test cases:
# test.assert_equals(number([]), [])
# test.assert_equals(number(["a", "b", "c"]), ["1: a", "2: b", "3: c"])

testing123(strang)
