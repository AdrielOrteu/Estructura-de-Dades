import copy
import time

class BlocNotes:
    
    class Nota:
        __slots__= ("_missatge","_data", "_time")
      
        def __init__(self,missatge):
            self._missatge = missatge
            self._time = time.strftime("%H:%M:%S")
        
        @property
        def missatge(self):
            pass
        @missatge.setter
        def missatge(self,missatge):
            pass
        

        @property
        def data(self):
            pass
        @data.setter
        def data(self,data):
            pass

        def __str__(self):
            pass
      
    __slots__= ("_notes")
  

    def __init__(self):
        self._notes :dict [str, str] = {}

    def add(self, nom, nota):
        if nom not in self._notes:
            self._notes[nom] = nota
    
    def elim(self, nom):
    
    def getNota(self,nom):
    
    
    def copy(self):
    
    
    def __str__(self):
        pass
  
if __name__ == "__main__":
    
    print("====CREEM b com a Bloc Notes i afegim 2 notes===")
    b=BlocNotes()
    b.add("N1","Dema classe ED")
    b.add("N2","Comprar memoria")
    
    nota = b.getNota("N1")
    print("===La nota N1 es:",nota)
    
    b1=b
    b2=copy.copy(b)
    b3=copy.deepcopy(b)
    
    print("===DESPRES DE FER COPIES===")
    print("===b val:")
    print(b)
    print("===b1 val:")
    print(b1)
    print("===b2 val:")
    print(b2)
    print("===b3 val:")
    print(b3)
    
    b2.add("N3","fer practica ED")
    b3.add("N4","revisar transpes ED")
    
    print("===DESPRES D'AFEGIR N3 a b2 i N4 a b3===")
    print("===b val:")
    print(b)
    print("===b1 val:")
    print(b1)
    print("===b2 val:")
    print(b2)
    print("===b3 val:")
    print(b3)
    
    b1.elim("N1")
    
    print("===DESPRES D'ELIMINAR N1 a b1===")
    print("===b val:")
    print(b)
    print("===b1 val:")
    print(b1)
    print("===b2 val:")
    print(b2)
    print("===b3 val:")
    print(b3)
    