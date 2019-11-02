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
from threading import Thread
import time

queue = FIFO()


class CloudGateway:

    def send(queue):
        while True:
            time.sleep(5)
            queue.pop()


device = Thread(target=CloudGateway.send, args=(queue,))
device.start()


@app.route("/")
@app.route("/iotserver")
def index():
    return render_template("index.html")


@app.route('/server', methods=['POST'])
def server():
    data = request.get_json()
    # adicionando no priorizador
    queue.push(data)

    return "ok", 200


@app.route("/list")
def list_fila():
    return render_template("prioridade.html", queue=queue)
