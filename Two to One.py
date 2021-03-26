# Two to One.py
#! python3
'''
Take 2 strings s1 and s2 including only letters from a to z. Return a new
sorted string, the longest possible, containing distinct letters,
each taken only once - coming from s1 or s2.
Examples:
a = 'xyaabbbccccdefww'
b = 'xxxxyyyyabklmopq'
longest(a, b) -> 'abcdefklmopqwxy'

a = 'abcdefghijklmnopqrstuvwxyz'
longest(a, a) -> 'abcdefghijklmnopqrstuvwxyz'
'''

# find unique letters in the combination of two strings


def twoToOne(s1, s2):
    combo = s1 + s2
    list1 = []
    newS = ''
    for i in combo:
        if i not in list1:
            list1.append(i)
    print('Returning Unique letters: \n')
    print('')
    return newS.join(list1)


# test cases
string1, string2 = 'xyaabbbccccdefww', 'xxxxyyyyabklmopq'
combo1 = 'xyaabbbccccdefww' + 'xxxxyyyyabklmopq'
twoToOne(string1, string2)
