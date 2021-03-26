# WeIrD StRiNg CaSe.py

"""
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string,
 and returns the same string with all even
  indexed characters in each word
 upper cased, and all odd indexed characters in each word lower cased.
 The indexing just explained is zero based, so the zero-ith index is even,
 therefore that character should be upper cased.

The passed in string will only consist of alphabetical characters and
spaces(' '). Spaces will only be present if there are multiple words.
 Words will be separated by a single space(' ').

Examples:
toWeirdCase('String'); # => returns 'StRiNg'
toWeirdCase('Weird string case') # => returns 'WeIrD StRiNg

"""

# sample data

sample = 'Weird string case'


def to_weird_case(string):
    listOwords = []
    for i in string.split():  # for each word
        weirdWord = []

        for index in range(len(i)):
            if index % 2 == 0:  # if index is even
                weirdWord.append(i[index].upper())
            else:
                weirdWord.append(i[index].lower())
        listOwords.append(''.join(weirdWord))
    return ' '.join(listOwords)


to_weird_case(sample)
