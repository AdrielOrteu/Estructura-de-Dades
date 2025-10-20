import random

class MapBase:
    class _Item:
        """Parella de clau,valor que es element de la taula hash o diccionari."""
        __slots__ = '__key' , '__value'
        
        def __init__ (self, k, v):
            self.__key = k
            self.__value = v
        
        def __eq__ (self, other):
            if isinstance(other, MapBase._Item):
                return self.__key == other.__key
            elif type(self.__key) == type(other):
                return self.__key == other
            else:
                raise TypeError("other must be an item of the Map")
        
        def __ne__ (self, other):
            return not (self == other)
        
        def __lt__ (self, other):
            if isinstance(other, MapBase._Item):
                return self.__key < other.__key
            elif  type(self.__key):
                return self.__key < other
            else:
                raise TypeError("other must be an item of the Map")
        
        def __str__(self):
            return self.__value.__str__()
        def __repr__(self):
            return self.__key.__repr__()
        
        @property
        def key(self):
            return self.__key
        @key.setter
        def key(self, n_key):
            self.__key = n_key
        
        @property
        def value(self):
            return self.__value
        @value.setter
        def value(self, n_value):
            self.__value = n_value

class MapUnsorted(MapBase): 
    #Definicio class Hash Simple sense funcio hash nomes accedeix per clau
    def __init__ (self):
        """Crea una taula hash buida."""
        self._items : list[MapBase._Item] = []
        self._size : int = 0
    
    def __getitem__ (self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        j = 0
        while k != self._items[i] and j < self._size:
            j += 1
        if j < self._size:
            return self._items[j].__value
        else:
            raise KeyError
    
    def __setitem__ (self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self._items:
            if k == item.key:
                item.value = v
                return
        self._items.append(self._Item(k=k, v=v))
        self._size += 1
    
    def __delitem__ (self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        for j in range(self._size):
            if self._items[j].key == k:
                self._items.pop(j)
                return
        raise KeyError

    def __len__ (self):
        """Return number of items in the map."""
        return self._size

    def __iter__ (self):
        """Generate iteration of the map s keys."""
        pass
    def __str__(self):
        pass
    def __repr__(self):
        pass


class Hash(MapBase):

    def __init__ (self,cap=11, p=109345121):
        """Crea una taula hash buida."""
        self.__scale = random.randint(a=1,b=p)
        self.__shift = random.randint(a=1,b=p)
        self.__prime : int = p
        self.__table : list[MapBase._Item | None] = cap*[None]
        self._cap = cap
        self._size = 0

    """ JA DONAT! """
    def __hash_function(self, k) -> int:
        return (hash(k)* self.__scale + self.__shift) % self.__prime % len(self.__table)

    def __iter__ (self) -> MapBase._Item:
        for item in self.__table:
            if item is not None:
                yield item
    def __getitem__ (self, k):
        """Retorna valor associat a clau k (raise KeyError si no el troba)."""
        v = self.__table[ self.__hash_function(k) ]
        if v is not None:
            if v.key == k:
                return v
        raise KeyError
    
    def __contains__ (self, k):
        try:
            self[k]
            return True
        except KeyError:
            return False
    
    def __setitem__ (self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        k_hash = self.__hash_function(k)
        if self.__table[k_hash] is None:
            self.__table[k_hash] = self._Item(k,v)
            self._size += 1
        elif self.__table[k_hash].key == k:
            self.__table[k_hash] = self._Item(k,v)
        else:
            self._resize(self._cap*2)
            self.__setitem__(k, v)
    
    def _resize(self, c: int):
        old_table = self.__table
        self.__table = [None] * c
        for item in old_table:
            if item is not None:
                k_hash = self.__hash_function(item.key)
                self.__table[k_hash] = item
    
    #def _my_resize(self,c:int):
    #    temp_table = [None]*c
    #    for item in self:
    #        temp_table[self.__hash_function(item.key)] = item
    #    self.__table = temp_table
    
    def __delitem__ (self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        k_hash = self.__hash_function(k)
        self.__table[k_hash] = None
        #if k == self.__table[k_hash].key:
        #    self.__table[k_hash] = None
        #    self._size -= 1
        #elif self.__table[k_hash] is not None:
        #    raise KeyError
    def __len__ (self):
        """Return number of items in the map."""
        return self._size
    
    def __str__(self):
        return self.__table.__str__()
    def __repr__(self):
        return self.__table.__repr__()


if __name__ == "__main__":
   
   grade=0
   print("Comment :=>>=====CREEM DICCIONARI=====\n") 
   h=Hash()
   grade+=0.5
   
   print("Comment :=>>=====MOSTRA DICCIONARI BUIT=====")
   print(h)
   print("\n")
   grade+=0.5
   
   l= [("Barcelona", "150 l/cm2"),
       ("Badalona",  "135 l/cm2"),
       ("Sabadell",   "75 l/cm2"),
       ("Cerdanyola", "55 l/cm2"),
       ("Bellaterra", "65 l/cm2")
      ]
   
   print("Comment :=>>=====INICIALITZEM DICCIONARI=====") 
   acceptat=[]
   for e in l:
       try:
           h[e[0]]=e[1]
           acceptat.append(True)
       except KeyError: # otherwise:
           print("Comment :=>> COLLISIO")
           acceptat.append(False)
   grade+=1
   
   print("Comment :=>>=====MOSTRA DICCIONARI AMB ITEMS=====")
   print(h)
   print("\n")
   grade+=0.5
   
   
   print("Comment :=>>=====CONSULTA DICCIONARI ITEMS EXISTENTS=====")
   for i in range(len(l)):       
       if acceptat[i] and l[i][0] in h:
           grade+=0.5
           print("Comment :=>>CORRECTE ", l[i][0], " EXISTEIX A LA TAULA HASH")
           
           print("Comment :=>>Definicio de ", l[i][0], " es: ", h[l[i][0]])
           if (h[l[i][0]]==l[i][1]):
               print("Comment :=>>Definicio CORRECTA \n")
               grade+=0.5
           else:
               print("Comment :=>>Definicio ERRONIA. LA DEFINICIO CORRECTA ES:",l[i][1], "\n")
       elif not(acceptat[i]) :
           print("Comment :=>>CORRECTE ", l[i][0], " HAURIA D'EXISTIR A LA TAULA HASH PERO VA PRODUIR UNA COLLISIO I NO EXISTEIX")
           grade+=1
       else:
           print("Comment :=>>ERROR ", l[i][0], " EXISTEIX A LA TAULA HASH. PERO HAS DIT QUE NO")
           
   print("\n")    
   
   print("Comment :=>>=====CONSULTA DICCIONARI ITEMS NO EXISTENTS ALGUNS PODEN TENIR COLLISIO DEPENENT DE NOMBRES ALEATORIS=====")
   if "Girona" in h:
       print("Comment :=>>ERROR Girona EXISTEIX A LA TAULA HASH")
       print("Comment :=>>Valor de Girona es: ", h["Girona"])
   else:
       print("Comment :=>>OK Girona NO EXISTEIX A LA TAULA HASH")
       h["Girona"] = "15 l/cm2"
       grade+=0.5
   print("\n")
   
   if "Girona" not in h:
       print("Comment :=>>ERROR Girona NO EXISTEIX A LA TAULA HASH")
   else:
       print("Comment :=>>OK Girona EXISTEIX A LA TAULA HASH")
       print("Comment :=>>Valor de Girona es: ", h["Girona"])
       grade+=0.5
   print("\n")
       
   if "Girona" in h:
       del h["Girona"]
       if "Girona" in h:
           print("Comment :=>>ERROR Girona ENCARA EXISTEIX A LA TAULA HASH")
           print("Comment :=>>Valor de Girona es: ", h["Girona"])
       else:
           print("Comment :=>>OK Girona NO EXISTEIX A LA TAULA HASH")
           grade+=0.5
   else:
       pass
   print("\n")
   
   print("Comment :=>>=====MOSTRA DICCIONARI DESPRES DE LES CONSULTES NO EXISTENTS=====")
   print(h)
   print("\n")
   grade+=1
   
   if (grade < 0):
       grade = 0.0
       print("Comment :=>> ------------------------------------------" )
   if (grade == 10.0):
       print("Comment :=>> Final del test sense errors" )

   print("Grade :=>> " , grade )

    

    