class LlistaN:
    """Llista simplement encadenada sense centinelles"""

################################Definicio Class _Node       
    class _Node:
        """Classe no publica que guardar nodes"""
        __slots__ = '_valor' , '_next' # streamline memory usage
        def __init__ (self, valor, next=None): # initialize node’s fields
            self._valor = valor # reference to user’s element
            self._next = next
        @property
        def next(self):
            return self._next
        @property
        def valor(self):
            return self._valor
        
        def __str__(self):
            return str(self._valor)

################################Definicio Class LlistaN       
    def __init__ (self,p1=None):
        """Create an empty list. or a list from an existing one"""
        self._first = None
        self._last = None
        self._size = 0         
        if type(p1)==list:
            for n in p1:
                 self.add_last(n)                                 
        elif type(p1) is type(self):
             for n in p1:
                 self.add_last(n.valor)                                 
                        
          
    def __len__ (self):
        """Return num elements llista"""
        return self._size
    @property
    def last(self):
        return self._last
    @property
    def first(self):
        return self._first
    
    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def __iter__ (self):
       #Generate iteration of the list.
        self._pos=self._first   
        return self
    
    def __next__ (self):
        #Generate iteration of the list.
        if (self._pos != None) :
            result = self._pos
            self._pos = self._pos._next
            return result
        else:# End of Iteration
            raise StopIteration
    
    def add_last(self,e):
        nouNode = self._Node(e,None)
        if (self._last != None):
            self._last._next = nouNode
            self._last = nouNode
        else:
            """Si llista buida"""
            self._last = nouNode
            self._first = nouNode
        self._size += 1
        return nouNode
    
    def _str_(self):
        cadena=""
        node = self._first
        while (node != None):
            cadena = cadena + "\n" + str(node)
            node = node._next
        return cadena
    
    def __repr__(self):
        return self._str_()

########## Per omplir a classe
    def cerca(self, valor):
        return self.cercaRecursiva(self._first, valor)
    
    def cercaRecursiva(self, nodeAct, valor):
        if nodeAct is None:
            return False
        elif nodeAct.valor == valor:
            return True
        else:
            return self.cercaRecursiva(nodeAct.next, valor)
        

    def printInvers(self):
        if self._first is None:
            return ""
        else:
            return self.printInversRec(self._first)
        
    def printInversRec(self,nodeAct):
        if nodeAct.next is None:
            return str(nodeAct)
        else:
            return self.printInversRec(nodeAct.next) + ", " + str(nodeAct)
    
    def printInversIter(self):
        pass
