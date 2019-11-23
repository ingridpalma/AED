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
from threading import Thread
import time
import json

queue = FIFO()
#queue = BinomialHeap()
#queue = Fheap()


class CloudGateway:

    def send(queue):

        start = time.time()
        while True:
            time.sleep(0.5)
            item = queue.pop()
            if item is None:
                continue

            total = time.time() - item["ts"]
            print("Priority Class: {0} | Queue Time: {1}".format(item["device_type"], total))

        #print("Tempo total: {0}".format(time.time() - start))
                #break;


# Binomial =  Tempo total: 0.0002810955047607422
# FIFO = Tempo total: 1.0967254638671875e-05

localGateway = Thread(target=CloudGateway.send, args=(queue,))
localGateway.start()


@app.route("/")
@app.route("/iotserver")
def index():
    return render_template("index.html")


@app.route('/server', methods=['POST'])
def server():
    data = request.get_json()
    data["ts"] = time.time()
    # adicionando no priorizador
    queue.push(data)
    return "ok", 200


@app.route("/list")
def list_fila():
    return render_template("prioridade.html", queue=queue)




