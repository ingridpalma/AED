#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 23:18:34 2019

@author: mic
"""
from app import app
from flask import render_template
from flask import jsonify, request

fifo = []
@app.route("/")
@app.route("/iotserver")
def index():    
    return render_template("index.html")

@app.route('/server', methods=['POST'])
def server():
    data = request.get_json()
    fifo.append(data)
    print (data["id"])
    return "ok", 200

@app.route("/list")
def list_fila():    
    return render_template("prioridade.html",fifo=fifo)


