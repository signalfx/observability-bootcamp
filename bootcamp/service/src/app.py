import json
import re
from flask import Flask, request, Response
import prometheus_client
from prometheus_client.exposition import CONTENT_TYPE_LATEST
from prometheus_client import Counter


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
c_recv = Counter('characters_recv', 'Number of characters received')
c_norm = Counter('characters_norm', 'Number of normalized characters processed')
c_word = Counter('words_processed', 'Number of words processed')


@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.route('/wordcount', methods=['POST'])
def wordcount():
    f = request.files['text']
    fn = f.filename
    print(fn)
    data = request.files['text'].read().decode('utf-8')
    c_recv.inc(len(data))

    text = normalize(data)
    c_norm.inc(len(text))

    wordstream = split(text)
    c_word.inc(len(wordstream))

    counts = count(wordstream)

    return json.dumps(sorted(counts.items(), key=lambda x: x[1])[-10:])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
