import os
from flask import Flask, request, redirect
import json
from chain import Chain
blockApp = Flask('BlockApp')


@blockApp.route("/blockchains/")
def blockchains():
    content = []
    for e in os.listdir('blocks/'):
        content.append(e)
    return json.dumps({'blockchains': content}, indent=4)


@blockApp.route("/blockchains/<blockchain>/")
def chain(blockchain):
    chain = Chain(blockchain)
    chain.loadChain(blockchain)
    return json.dumps({'blocks': chain.blocksToJson()}, indent=4)


@blockApp.route("/blockchains/<blockchain>/<block>/")
def block(blockchain, block):
    with open('blocks/{}/{}.json'.format(blockchain, block)) as file:
        data = json.load(file)
        content = []
        for t in data['transactions']:
            content.append(t)
        return json.dumps({'transactions': content}, indent=4)


