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


def _normalize(text):
    lower = text.lower()
    return letter_only(lower)


app = Flask(__name__)
c_norm = Counter('characters_norm', 'Number of normalized characters processed')


@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.route('/api', methods=['POST'])
def normalize():
    data = request.get_json()

    text = _normalize(data['text'])
    c_norm.inc(len(text))

    return json.dumps(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
