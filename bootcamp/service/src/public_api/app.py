import json
import os
import re
from flask import Flask, request, Response
import prometheus_client
from prometheus_client.exposition import CONTENT_TYPE_LATEST
from prometheus_client import Counter
import redis
import requests
import random
from opentelemetry import trace


def _normalize(text):
    res = requests.post('http://normalize:5000/api', json={'text': text})
    return res.json()


def _split(text):
    res = requests.post('http://split:5000/api', json={'text': text})
    return res.json()


def _count(text):
    res = requests.post('http://count:5000/api', json={'text': text})
    return res.json()


app = Flask(__name__)
r = redis.Redis.from_url(os.getenv('REDIS_URL'))
c_recv = Counter('characters_recv', 'Number of characters received')


@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.route('/api', methods=['POST'])
def wordcount():
    file = request.files['text']
    fn = file.filename

    cached = r.get(fn)
    
    choice = random.choice(["blue", "green", "red"])
    trace.get_current_span().set_attribute("color", choice)
    trace.get_current_span().set_attribute("fileName", fn)

    if cached is not None:
        result = cached
    else:
        data = file.read().decode('utf-8')
        c_recv.inc(len(data))

        text = _normalize(data)
        wordstream = _split(text)
        counts = _count(wordstream)

        result = json.dumps(counts)
        r.set(fn, result)

    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0')
