# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 17:10:56 2019

@author: gemma
"""
import math

import copy
from copy import deepcopy


class Point:
    
      def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y
      
      @property
      def x(self):
        return self._x
      @x.setter
      def x(self, valor):
        self._x = valor
      
      @property
      def y(self):
        return self._y
      @y.setter
      def y(self, valor):
        self._y = valor
      def __sub__(self,p2):
        return math.sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)
    
      def __str__(self):
        return "("+ str(self.x) + ", " + str(self.y) + ")"
      
    
class Poligon:
     
    maxim = 1000
    def __init__(self):
        self._vertexs = []
        
    def afegeixVertex(self, pt):
        # self._vertexs.append(pt)
        # self._vertexs.append(Point(pt.x, pt.y))
        self._vertexs.append(deepcopy(pt))
        
    def __str__(self):
        l=""
        for i in self._vertexs:
            l += str(i)
        return l
        
if __name__ == "__main__":
    
    p1=Point(1,2)
    p2=Point(4,5)
    p3=Point(8,9)
    p4=Point(10,21)
    
    pol1=Poligon()
    pol1.afegeixVertex(p1)
    pol1.afegeixVertex(p2)
    pol1.afegeixVertex(p3)
    pol1.afegeixVertex(p4)
    print(pol1)
    
    p1.x=99
    
    print(pol1)
    