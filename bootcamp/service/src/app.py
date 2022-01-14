import re
from unicodedata import category


def letter_only(text):
    return re.sub("[^\w' ]", "",
             re.sub("[^\w']", " ", text))


def normalize(text):
    lower = text.lower()
    return letter_only(lower)


def split(text):
    return text.split()


def count(text):
    words = {}
    for word in text:
        if word not in words:
            words[word] = 0
        words[word] += 1

    return words


with open("hamlet.txt", encoding="UTF-8") as file:
    hamlet = file.read()
text = normalize(hamlet)
wordstream = split(text)
counts = count(wordstream)

print(sorted(counts.items(), key=lambda x: x[1])[-10:])
