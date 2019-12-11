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

    def send(queue, file):

        while True:
            time.sleep(0.1)
            item = queue.pop()
            if item is None:
                continue

            total = time.time() - item["ts"]
            file.write("{0};{1}\n".format(item["device_type"], total))
            file.flush()


    def sendVEB(queue, file, dd):

        while True:
            #time.sleep(0.1)
            item = queue.pop()
            if item is None:

                continue

            item = dd[item][0]
            total = time.time() - item["ts"]
            file.write("{0};{1}\n".format(item["device_type"], total))
            file.flush()


fifoImpl = FIFO()
binomialImpl = BinomialHeap()
fibImpl = Fheap()
vebImpl = VEB(33554432)

dd = defaultdict(list)

file_veb = open('result_veb_1000.csv'.format(time.time()), 'w')
localGateway_veb = Thread(target=CloudGateway.sendVEB, args=(vebImpl, file_veb, dd))
localGateway_veb.start()

file_fifo = open('result_fifo_1000.csv'.format(time.time()), 'w')
localGateway_fifo = Thread(target=CloudGateway.send, args=(fifoImpl, file_fifo))
localGateway_fifo.start()

file_binomial = open('result_binomial_1000.csv'.format(time.time()), 'w')
localGateway_binomial = Thread(target=CloudGateway.send, args=(binomialImpl, file_binomial))
localGateway_binomial.start()

file_fib = open('result_fib_1000.csv'.format(time.time()), 'w')
localGateway_fib = Thread(target=CloudGateway.send, args=(fibImpl, file_fib))
localGateway_fib.start()


@app.route("/")
@app.route("/iotserver")
def index():
    return render_template("index.html")

@app.route('/fifo', methods=['POST'])
def fifo():
    data = request.get_json()
    data["ts"] = time.time()
    fifoImpl.push(data)
    return "ok", 200

@app.route('/binomial', methods=['POST'])
def binomial():
    data = request.get_json()
    data["ts"] = time.time()
    binomialImpl.push(data)
    return "ok", 200

@app.route('/fib', methods=['POST'])
def fib():
    data = request.get_json()
    data["ts"] = time.time()
    fibImpl.push(data)
    return "ok", 200


@app.route('/veb', methods=['POST'])
def veb():
    data = request.get_json()
    data["ts"] = time.time()

    if data["device_type"] == 1:
        key = 100000 + len(dd)
    elif data["device_type"] == 2:
        key = 200000 + len(dd)
    elif data["device_type"] == 3:
        key = 300000 + len(dd)

    dd[key].append(data)
    vebImpl.push(key)
    return "ok", 200


@app.route("/list")
def list_fila():
    return render_template("prioridade.html", queue=fifo)