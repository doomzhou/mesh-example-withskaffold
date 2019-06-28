#!/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
import requests

app = Flask(__name__)
app.secret_key = "snthaoeutnNaToheu"


@app.route('/')
def index():
    '''
    index
    '''
    s2_domain = 'mesh-ex2'
    try:
        res = requests.get('http://{}'.format(s2_domain)).text
    except Exception as e:
        res = e
    code = 0 if res else 1
    return jsonify({'code': code, 'msg': "{}".format(res)})


if __name__ == '__main__':
    app.run(port=8060, debug=True)
