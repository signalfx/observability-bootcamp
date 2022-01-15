import json
import re
from flask import Flask, request, Response
import prometheus_client
from prometheus_client.exposition import CONTENT_TYPE_LATEST
from prometheus_client import Gauge


def count(text):
    words = {}
    for word in text:
        if word not in words:
            words[word] = 0
        words[word] += 1

    return words


app = Flask(__name__)
c_words = Gauge('words_count', 'Number of unique words')
c_words.set(0)


@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.route('/api', methods=['POST'])
def wordcount():
    data = request.get_json()
    counts = count(data['text'])
    c_words.set(len(counts))

    return json.dumps(sorted(counts.items(), key=lambda x: x[1])[-10:])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
