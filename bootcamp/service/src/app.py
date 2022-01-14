import json
import re
from flask import Flask, request, Response


def letter_only(text):
    return re.sub(r"\s+", " ",
                  re.sub(r"[^\w' ]", "",
                         re.sub(r"[^\w']", " ", text)))


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


app = Flask(__name__)


@app.route('/wordcount', methods=['POST'])
def wordcount():
    data = request.files['text'].read().decode('utf-8')
    text = normalize(data)
    wordstream = split(text)
    counts = count(wordstream)

    return json.dumps(sorted(counts.items(), key=lambda x: x[1])[-10:])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
