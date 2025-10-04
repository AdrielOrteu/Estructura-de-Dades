# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:39:10 2019

@author: gemma
"""
import copy
from copy import deepcopy


class Pila:
    #LIFO
    def __init__ (self,l=None):
        if l is None:
            self.data = list()
        else:
            list(l)
    def __len__ (self):
        return len(self.data)
    
    def is_empty(self):
        return len(self.data) == 0
    
    def push(self, e):
        self.data.append(e)
        
    def top(self):
        """Retorna element al top (pero no esborra) Raise Empty exception si pila buida"""
        if self.is_empty():
            raise ValueError("Can't pop element from empty Stack")
        return deepcopy(self.data[-1])
    
    def pop(self):
        """Esborra i retorna element al top Raise Pila Buida exception si pila buida"""
        if self.is_empty():
            raise ValueError("Can't pop element from empty Stack")
        temp = self.top()
        self.data.pop()
        return temp
    def __str__(self):
        """ per poder printar cua"""
        return f"{self.data} | top : {self.top()}"
#    def __repr__(self):
        """per poder visualitzar cua quan escrivim nom objecte del tipus"""
#        return
if __name__ == "__main__":
    p=Pila([1,2,3,4])
    print(p.top())
    print("Longitud: ",len(p))
    p.pop()
    print(p.top())
    p.pop()
    print(p.top())
    p.pop()
    print(p.top())
    p.pop()
    if (p.is_empty()):  
      print("Esta buida")
    p.push(89)
    print(p.top())

    