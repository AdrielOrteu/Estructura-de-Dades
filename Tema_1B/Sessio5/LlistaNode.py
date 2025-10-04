# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:39:10 2019

@author: gemma
"""
class LlistaN:
    """Llista simplement encadenada sense centinelles"""
    
    
    
    ################################Definicio Class __Node
    class __Node:
        __slots__ ="__valor", "__n"
        """Classe no publica que guardar nodes"""
        
        def __init__(self, valor, n=None):
            self.__valor = valor
            self.__n = n
        
        @property
        def valor(self):
            return self.__valor
        @valor.setter
        def valor(self, value):
            self.__valor = value
        
        @property
        def next(self):
            return self.__n
        @next.setter
        def next(self, value):
            self.__n = n
        
        def __str__(self):
            return self.__valor.__str__()
    ################################Definicio Class LlistaN
    def __init__ (self,l=None):
        self._first = None
        self._last = None
        self._size = 0
        #Create an empty list. or a list from an existing one
    
    def __len__ (self):
        return self._size
        #Return num elements llista
    
    @property
    def last(self):
        pass
    
    @property
    def first(self):
        pass
    
    
    def is_empty(self):
        return self._size == 0
        #Return True if list is empty.
    def add_node(self, e, predecessor):
        #Afegeix e entre 2 node existents i rentorna node nou.
        # node = self.__Node(e, predecessor)
        pointer = self._first.next
        node_found = pointer is predecessor
        while not node_found:
            pointer = pointer.next
    
    def add_last(self,e):
        node = self.__Node(e, None)
        if self.is_empty():
            self._first = node
        self._last = node
        
        self._size += 1
    
    def add_first(self,e):
        if self.is_empty():
            node = self.__Node(e, None)
            self._last = node
        else:
            node = self.__Node(e, self._first)
        self._first = node
        self._size += 1
    
    def delete_last(self):
        pass
        #Esborra ultim node i retorna el valor.
    
    def delete_next(self, predecessor):
        pass
        #Delete node seguent a predecessor i retorna el valor.
    
    def delete_first(self):
        pass
    #Delete first node i retorna el valor.
    
    def __str__(self):
        pass
    
    def __repr__(self):
        pass

    
if __name__ == "__main__":
    l=LlistaN()
    if l.is_empty():
        print("Buida")
    else:
        print("No Buida")
        print( l)
    
    for i in range(10):
        l.add_last(i)
        
    print(l)
    
    l.add_node(-1,None)
    print(l)
    
    l.delete_last()
    print(l)
    
    print ("Longitud: ", len(l))
    
    if l.is_empty():
        print("Buida")
    else:
        print("No Buida")
        print(l)
    
    node = l.first
    l.add_node(-2,None)
    print(l)
    
    l.add_node(-3,l.first)
    print(l)
    
    l.add_node(-4,l.last)
    print (l)
    
    
    for n in l:
        print(n)
    
    l2=LlistaN(l)
    print (l2)
    