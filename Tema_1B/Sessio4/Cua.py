# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:51:40 2019

@author: gemma
"""
import copy
from copy import deepcopy


class Cua:
 
    def __init__ (self, l=None):
        """Crea cua"""
        if l is None:
            self._data = list()
        else:
            self._data = list(l)
        
        self._head=0
        self._tail=len(self)
    def __len__ (self):
        """Retorna el nombre d'elements de la cua"""
        return len(self._data)

    def is_empty(self):
        """Retorna True si la cua es buida."""
        return self._head == self._tail
    def primer(self):
        """Retorna primer element sense eliminar
        dona error si cua buida
        """
        if self.is_empty():
            raise BaseException("Empty")
        return self._data[self._head]
     
    def desencua(self):
        """Esborra i retorna 1er element cua (i.e., FIFO).
        Excepcio si cua buida
        """
        r = self.primer()
        self._tail -= 1
        self._data.remove(r)
        return r
  
    def encua(self, e):
        """Afegeix el al final cua"""
        if self._tail == len(self):
            self.__resize(self._tail + 1)
        self._tail += 1
        
        self._data[self._tail] = e
  
    def __resize(self, cap): # we assume cap >= len(self)
        """Fa mes gran la capacitat de la llista quan esta plena."""
        temp = deepcopy(self._data)
        self._data = [None]*self._tail
        for j in range(cap):
            self._data[i] = temp[j]
    def __str__(self):
        """ per poder printar cua"""
        return self._data.__str__()
    def __repr__(self):
        """per poder visualitzar cua quan escrivim nom objecte del tipus"""
        return self._data.__repr__()

 
if __name__ == "__main__":
    print("CREO CUA BUIDA")
    c=Cua()
    print("OMPLO CUA AMB NOMBRES DE 0 a 8")
    for i in range(8):
        c.encua(i)
    print("VEIG CUA")
    c
    print("TREC ELEMENT CUA")
    c.desencua()
    print("VEIG CUA")
    c
    
    print("CREO CUA [1,2,3,4]")
    c2=Cua([1,2,3,4])
    print("PRIMER ELEMENT CUA:",c2.primer())
    print("Longitud CUA: ",len(c2))
    print("TREC PRIMER ELEMENT CUA [1,2,3,4]")
    c2.desencua()
    print("PRIMER ELEMENT CUA:",c2.primer())
    print("TREC PRIMER ELEMENT CUA [2,3,4]")
    c2.desencua()
    print("PRIMER ELEMENT CUA:",c2.primer())
    print("TREC PRIMER ELEMENT CUA [3,4]")
    c2.desencua()
    
    print("PRIMER ELEMENT CUA:",c2.primer())
    print("TREC PRIMER ELEMENT CUA [4]")
    c2.desencua()
    if (c2.is_empty()):  
      print("Esta buida")
    print("AFEGIR 34 A CUA []")
    c2.encua(34)
    print("MIRO PRIMER ELEMENT CUA [34]:",c2.primer())
    
    print("CREO CUA BUIDA")
    c3=Cua()
    print("AFEGIR 8 A CUA []")
    c3.encua(8)
    print("PRINTO CUA [8]")
    print(c3)
    print("MIRO CUA [8]")
    c3
    

    