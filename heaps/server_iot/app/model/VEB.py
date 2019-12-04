#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:44:31 2019

@author: mic
"""

# Fonte : https://github.com/erikwaing/VEBTree/blob/master/VEB.py -  com customizacao https://github.com/eng.maribeiro
from collections import deque
import math
import json
import ast


class VEB:

    def __init__(self, u):
        if u < 0:
            raise Exception("u não pode ser menor que 0 --- u = " + str(u));
        self.u = 2;
        while self.u < u:
            self.u *= self.u
        self.min = None
        self.max = None
        if (u > 2):
            self.clusters = [None for i in range(self.high(self.u))]  # VEB(self.high(self.u))
            self.summary = None  # VEB(self.high(self.u))

    def high(self, x):
        return int(math.floor(x / math.sqrt(self.u)))

    def low(self, x):
        return int((x % math.ceil(math.sqrt(self.u))))

    def index(self, x, y):
        return int((x * math.floor(math.sqrt(self.u))) + y)

    def member(self, x):
        if x == self.min or x == self.max:  # found it as the minimum or maximum
            return True
        elif self.u <= 2:  # has not found it in the "leaf"
            return False
        else:
            cluster = self.clusters[self.high(x)]
            if cluster != None:
                return cluster.member(self.low(x))  # looks for it in the clusters inside
            else:
                return False

    def successor(self, x):
        if self.u <= 2:
            if x == 0 and self.max == 1:
                return 1
            else:
                return None
        elif self.min != None and x < self.min:  # x is less than everything in the tree, returns the minimum
            return self.min
        else:
            h = self.high(x)
            l = self.low(x)
            maxlow = None
            cluster = self.clusters[h]
            if cluster != None:
                maxlow = cluster.max
            if maxlow != None and l < maxlow:
                offset = cluster.successor(l)
                return self.index(h, offset)
            else:
                succcluster = None
                if self.summary != None:
                    succcluster = self.summary.successor(h)
                if succcluster == None:
                    return None
                else:
                    cluster2 = self.clusters[succcluster]
                    offset = 0
                    if cluster2 != None:
                        offset = cluster2.min
                    return self.index(succcluster, offset)

    def predecessor(self, x):
        if self.u <= 2:
            if x == 1 and self.min == 0:
                return 0
            else:
                return None
        elif self.max != None and x > self.max:
            return self.max
        else:
            h = self.high(x)
            l = self.low(x)
            minlow = None
            cluster = self.clusters[h]
            if cluster != None:
                minlow = cluster.min
            if minlow != None and l > minlow:
                offset = cluster.predecessor(l)
                if offset == None:
                    offset = 0
                return self.index(h, offset)
            else:
                predcluster = None
                if self.summary != None:
                    predcluster = self.summary.predecessor(h)
                if predcluster == None:
                    if self.min != None and x > self.min:
                        return self.min
                    else:
                        return None
                else:
                    cluster2 = self.clusters[predcluster]
                    offset = 0
                    if cluster2 != None:
                        offset = cluster2.max
                    return self.index(predcluster, offset)

    def emptyInsert(self, x):
        self.min = x
        self.max = x

    def insert(self, x):
        if self.min == None:
            self.emptyInsert(x)
        else:
            if x < self.min:
                temp = self.min
                self.min = x
                x = temp
            if self.u > 2:
                h = self.high(x)
                if self.clusters[h] == None:
                    self.clusters[h] = VEB(self.high(self.u))
                if self.summary == None:
                    self.summary = VEB(self.high(self.u))
                if self.clusters[h].min == None:
                    self.summary.insert(h)
                    self.clusters[h].emptyInsert(self.low(x))
                else:
                    self.clusters[h].insert(self.low(x))
            if x > self.max:
                self.max = x

    def delete(self, x):
        if self.max == self.min:
            self.min = None
            self.max = None
        elif (self.u == 2):
            if (x == 0):
                self.min = 1
            else:
                self.min = 0
        # encontra a proxima chaselfe e marca como o minimo
        else:

            if (x == self.min):
                first_cluster = self.summary.min
                x = self.index(first_cluster, self.clusters[first_cluster].min)
                self.min = x

            h = self.high(x)
            low = self.low(x)

            self.clusters[h].delete(low)
            # apos deletar deve-se verificar se o minimo e nulo e deletar do sumario tambem
            if (self.clusters[h].min == None):
                self.summary.delete(h)
                # After the above condition, if the key
                # is maximum of the treethen...
                if (x == self.max):
                    max_summary = self.summary.max
                    # If the max value of the summary is null
                    # then only one key is present so
                    # assign min. to max.
                    if (max_summary == None):
                        self.max = self.min
                    else:
                        self.max = self.index(max_summary, self.clusters[h].max)
            elif (x == self.max):
                self.max = self.index(h, self.clusters[h].max)

    def extract_min(self):
        if self.max == None and self.min==None:
           return None
        self.delete(self.min)
        return self.min


    def push(self, item):
        self.insert(json.dumps(item))

    def pop(self):
        r = self.extract_min()
        if r is not None:
            return ast.literal_eval(r)
        return r


'''
veb = VEB(1024)

veb.insert(100)
veb.insert(123)
veb.insert(50)
veb.insert(25)
veb.insert(10)
veb.insert(5)

print(veb.min)
veb.delete(veb.min)
print(veb.min)
veb.delete(veb.min)
print(veb.min)
veb.delete(veb.min)
print(veb.min)
veb.delete(veb.min)
print(veb.min)
veb.delete(veb.min)
print(veb.min)
veb.delete(veb.min)
print(veb.min)

'''