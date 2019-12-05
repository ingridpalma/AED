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
import ast
from collections import defaultdict


class CloudGateway:

    def send(queue, file, dd):

        while True:
            time.sleep(0.1)
            item = queue.pop()
            if item is None:
                continue

            #print("Item retornado {0}".format(item))
            item = dd[item][0]
            #print(item["device_type"])
            total = time.time() - item["ts"]
            #file.write("Priority Class: {0} | Queue Time: {1}\n".format(item["device_type"], total))
            file.write("{0};{1}\n".format(item["device_type"], total))
            file.flush()



#queue = FIFO()
#queue = BinomialHeap()
#queue = Fheap()
queue = VEB(33554432)
dd = defaultdict(list)

file = open('result_veb_100.csv'.format(time.time()), 'w')
localGateway = Thread(target=CloudGateway.send, args=(queue, file, dd))
localGateway.start()


@app.route("/")
@app.route("/iotserver")
def index():
    return render_template("index.html")


@app.route('/server', methods=['POST'])
def server():
    data = request.get_json()
    data["ts"] = time.time()

    if data["device_type"] == 1:
        key = 100000 + len(dd)
    elif data["device_type"] == 2:
        key = 200000 + len(dd)
    elif data["device_type"] == 3:
        key = 300000 + len(dd)

    #print("INSERIDO {0}".format(key))
    dd[key].append(data)
    queue.push(key)
    return "ok", 200


@app.route("/list")
def list_fila():
    return render_template("prioridade.html", queue=queue)