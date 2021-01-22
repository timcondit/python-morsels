# count.py
#
# I want you to write a function that accepts a string and returns a mapping (a
# dictionary or dictionary-like structure) that has words as the keys and the
# number of times each word was seen as the values.
#
# Your function should work like this:
#
# >>> count_words("oh what a day what a lovely day")
# {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
# >>> count_words("don't stop believing")
# {"don't": 1, 'stop': 1, 'believing': 1}

import re

def count_words(words):
    regex = r"\w+?'\w+|\w+"
    wordslist = re.findall(regex, words)
    #wordslist = words.split(" ")
    wordsdict = {}
    for word in wordslist:
        word = word.lower()
        if word in wordsdict:
            wordsdict[word] += 1
        else:
            wordsdict[word] = 1
    return wordsdict


if __name__ == "__main__":
    print(count_words("oh what a day what a lovely day"))
    print(count_words("Oh what a day what a lovely day"))
    print(count_words("Oh what a day, what a lovely day!"))
    print(count_words("don't stop believing"))
