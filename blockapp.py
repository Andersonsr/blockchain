import os
from flask import Flask, abort
from flask_api import status
import json
from chain import Chain
blockApp = Flask('BlockApp')


@blockApp.route("/blockchains/")
def blockchains():
    content = []
    for e in os.listdir('blocks/'):
        content.append(e)
    return json.dumps({'blockchains': content}, indent=4), status.HTTP_200_OK


@blockApp.route("/blockchains/<blockchain>/")
def chain(blockchain):
    chain = Chain(blockchain)
    try:
        chain.loadChain(blockchain)
    except FileNotFoundError:
        abort(404)
    return json.dumps({'blocks': chain.blocksToJson()}, indent=4), status.HTTP_200_OK


@blockApp.route("/blockchains/<blockchain>/<block>/")
def block(blockchain, block):
    try:
        with open('blocks/{}/{}.json'.format(blockchain, block)) as file:
            data = json.load(file)
            content = []
            for t in data['transactions']:
                content.append(t)
            return json.dumps({'transactions': content}, indent=4), status.HTTP_200_OK
    except FileNotFoundError:
        abort(404)

