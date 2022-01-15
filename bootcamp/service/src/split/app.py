import json
import re
from flask import Flask, request, Response
import prometheus_client
from prometheus_client.exposition import CONTENT_TYPE_LATEST
from prometheus_client import Counter


def _split(text):
    return text.split()


app = Flask(__name__)
c_word = Counter('words_processed', 'Number of words processed')


@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.route('/api', methods=['POST'])
def split():
    data = request.get_json()
    wordstream = _split(data['text'])
    c_word.inc(len(wordstream))

    return json.dumps(wordstream)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
