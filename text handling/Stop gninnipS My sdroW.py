# self explanatory

sample = r'This is a example of a sentence containing multiple words'


def spinWords(sentence):
    wordList = sentence.split()
    counter = 0
    longWords = {}

    for word in wordList:
        if len(word) >= 5:
            flip = word[::-1]
            longWords[counter] = word
            counter += 1
        else:
            counter += 1

    return longWords


spinWords(sample)
