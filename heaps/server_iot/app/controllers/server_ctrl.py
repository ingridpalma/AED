#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 23:18:34 2019

@author: mic
"""
from app import app
from flask import render_template
from flask import jsonify, request
from ..model.FIFO import FIFO
from ..model.BinomialHeap import BinomialHeap
from ..model.FibonacciHeap import Fheap
from ..model.VEB import VEB
from threading import Thread
import time
import json


class CloudGateway:

    def send(queue, file):

        while True:
            time.sleep(0.5)
            item = queue.pop()
            if item is None:
                continue

            total = time.time() - item["ts"]
            file.write("Priority Class: {0} | Queue Time: {1}\n".format(item["device_type"], total))
            file.flush()


#queue = FIFO()
#queue = BinomialHeap()
#queue = Fheap()
queue = VEB(1024)

file = open('result_veb.txt'.format(time.time()), 'w')
localGateway = Thread(target=CloudGateway.send, args=(queue, file,))
localGateway.start()


@app.route("/")
@app.route("/iotserver")
def index():
    return render_template("index.html")


@app.route('/server', methods=['POST'])
def server():
    data = request.get_json()
    data["ts"] = time.time()
    queue.push(data)
    return "ok", 200


@app.route("/list")
def list_fila():
    return render_template("prioridade.html", queue=queue)