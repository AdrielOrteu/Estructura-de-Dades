import sys
    
class BinaryTree:
    __slots__= '_valor','_pare','_left','_right'
    
    def __init__(self,valor=None,pare=None,FE=None,FD=None):
            self._valor=valor
            self._pare = pare
            self._left = FE
            self._right = FD
        
    
    def read(self,nomF):
        with open(nomF,"rt") as file:
            line = file.readline()
            if line: 
                h=int(line)
                line = file.readline()
                if line: 
                    v = line.split()
                    if len(v)>1:
                        self._addArrel(h,int(v[1]) if v[1].isdigit() else v[1])
                        self.llegirTreeRec(h,file,"ESQ")                                            
                        self.llegirTreeRec(h,file,"DRET")                                            
                            
    def llegirTreeRec(self,h,file,tipFillED):
        if (h > 0):
            line = file.readline()
            if line: 
                val = line.split()
                if len(val)>1:
                    nodPareAct=None
                    #Creem arrel del subarbre actual                   
                    if (tipFillED=="ESQ"):
                        #subarbre actual sera fill esquerre del seu pare
                        nodPareAct=self._addLeft( int(val[1]) if val[1].isdigit() else val[1])                        
                    else:
                        #subarbre actual sera fill dret del seu pare                        
                        nodPareAct=self._addRight( int(val[1]) if val[1].isdigit() else val[1])                        
                    #Creem fill esquerre
                    h-=1                   
                    nodPareAct.llegirTreeRec(h,file,"ESQ")
                    #Creem fill dret
                    nodPareAct.llegirTreeRec(h,file,"DRET")

    def _addArrel(self, h,v):
        """Posa v com a valor de l'arrel a un BinaryTree buit. Raise error si Tree no esta buit"""
        if self._valor is not None: raise sys.ValueError( "Arrel ja existeix")
        self._valor= v
        

    def _addLeft(self, v):
        """Crea fill left i posa _valor v
        retorna node creat que es un binaryTree
        """                        
        if self._valor is not None:
            self._left = BinaryTree(v,self)
        return self._left

    def _addRight(self, v):
        """Crea fill right i posa _valor v
        retorna node creat que es un binaryTree
        """                
        if self._valor is not None:
            self._right = BinaryTree(v,self)
        return self._right

    #=== Funcions auxiliars ===

    def __len__(self):
        #Retorna el nombre total delements a larbre
        l=1
        if self._left is not None:
            l= l + len(self._left)
        if self._right is not None:
            l= l + len(self._right)
        return l

    def __str__(self):
        if self._valor is not None:
            return self.escriuIdent(0)
        else:
            return ""

    def escriuIdent(self, depth):        
        cadRes = "Comment :=>> " + 2 * depth * " " + str(self._valor)+"\n"
        if self._left is not None:
            cadRes += self._left.escriuIdent(depth+1)
        if self._right is not None:
            cadRes += self._right.escriuIdent(depth+1)        
        return cadRes    

    #=== CODI Arbres I ===

    def esArrel(self):
        return self._pare is None
    
    def esFulla(self):
        return self._left is None and self._right is None
    
    def esBuit(self):
        return self._valor is None
    
    def profunditat(self):
        if self.esArrel():
            return 0
        else:
            return self._pare.profunditat() + 1
    def profunditatAlex(self):
        p = 0
        node_actual = self
        while not node_actual.esArrel():
            p += 1
            node_actual = node_actual._pare
        return p
    #---

    def fills(self):
        # Genera iteració de les posicions representant els fills de self
        if self._left is not None: yield self._left
        if self._right is not None: yield self._right
    
    def alcada(self):
        if self.esFulla():
            return 0
        return max( fill.alcada for fill in self.fills() ) + 1
    
    #---
    
    def germa(self): # Retorna node germà ó 'None' si no en té cap
        if self.esArrel():
            return None
        if self is self._pare._left:
            return self._pare._right
        return self._pare._left
    #---
    
    def grauNode(self):        
        if self._left is None:
            if self._right is None:
                return 0
            else:
                return 1
        else:
            if self._right is None:
                return 1
            else:
                return 2

    def grauTree(self):
        if self.esFulla():
            return 0
        elif self.grauNode() == 2:
            return 2
        return max(self.grauNode(), max( fill.grauTree() for fill in self.fills() ) )
    
    #--- Recorreguts
    
    def preordre(self):
        # TODO not finished, check yield hierarchy
        if self.esBuit():
            return None
        self.preordreRec()
    
    def preordreRec(self):
        yield self
        for fill in self.fills():
            fill.preordreRec()
    
    #---

    def mostraExpressio(self):
        pass# Exercici 6

    def inordre(self):
        if self.esBuit():
            return None
        return self.inorderRec()
    def inorderRec(self):
        if self._left is not None:
            yield self._left.inorderRec()
        yield self
        if self._right is not None:
            yield self._right.inorderRec()
        

    #---

    def cerca(self, val):
        if self._valor == val:
            return self
        elif self._valor < val:
            if self._right is not None:
                return self._right.cerca(val)
            else:
                return None
        else:
            if self._left is not None:
                return self._left.cerca(val)
            else:
                return None

