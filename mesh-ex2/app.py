#!/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from datetime import datetime
import requests

app = Flask(__name__)
app.secret_key = "snthao"


@app.route('/')
def index():
    '''
    index
    '''
    datestr = datetime.strftime(datetime.now(), '%x %X')
    return datestr


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8060, debug=True)
