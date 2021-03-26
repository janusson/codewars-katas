# Who likes it.py
# python3
"""
You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input
array, containing the names of people who like an item. It must return the
display text as shown in the examples:

likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2
others like this"
For 4 or more names, the number in and 2 others simply increases.
"""


import numpy as np

# function to check number of 'likes'


def likes(list1):
    # list1 must be some array of names
    if isinstance(list1, list):
        if len(list1) == 1:
            return str(f'{list1[0]} likes this')
        elif len(list1) == 2:
            return str(f'{list1[0]} and {list1[1]} like this')
        elif len(list1) == 3:
            return str(f'{list1[0]}, {list1[1]} and {list1[2]} like this')
        elif len(list1) > 3:
            return str(f'{list1[0]}, {list1[1]} and ' +
                       str(len(list1) - 2) + ' others like this')
        else:
            return str('no one likes this')


# test cases
people = 'James, Elyse, Adam, Alannah, Joel'.split(', ')
randomList = people[np.random.randint(0, len(people)):
                    np.random.randint(0, len(people))]

"""
# other string examples...

# str.format and C-style (%)

# adding information using str.format formatting:

for name in randomList:
    details = {'name': name, 'order': int(randomList.index(name) + 1)}
    print(('Name: {name} \n List' +
           ' Order: {order}').format(**details))


# using older C-style formatiing:

for name in randomList:
    order = int(randomList.index(name) + 1)
    print('Hello, %s' % name)
    print('You are in list position #%d' % order + '\n')

"""
