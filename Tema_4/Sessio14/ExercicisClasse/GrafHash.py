class GrafHash:
    """Graf amb Adjacency Map structure"""

################################ Definicio Class _Vertex

    class Vertex:
        __slots__ = '_valor'

        def __init__(self, x):
            self._valor=x
                  
        def __str__(self):
            return str(self._valor)
        
        def __eq__(self, other):
            return other == self._valor
        
        def __hash__(self):
            return self._valor.__hash__()
    
################################
    
    def __init__(self, ln=[],lv=[], lp=[]):
        """Crea graf (no dirigit per defecte, digraf si dirigit es True."""
        self._nodes = { }
        self._out : dict[GrafHash.Vertex, dict[GrafHash.Vertex, int|float]] = { }
        for n in ln:
            self.insert_vertex(n)
        if lp:
            for x, p in zip(lv, lp):
                self.insert_edge(x[0], x[1], p)
        else:
            for x in lv:
                self.insert_edge(x[0], x[1])

    def getOut(self):
        return self._out
            
    def insert_vertex(self, x):
        v = GrafHash.Vertex(x)
        self._nodes[x] = v
        self._out[v] = {}
    def insert_edge(self, n1, n2, w=1):
        self._out[n1][n2] = w
        self._out[n2][n1] = w
    
    def vertices(self):
        """Return una iteracio de tots els vertexs del graf."""
        return self._nodes.__iter__()
    
    def edges(self,x):
        """Return una iteracio de tots els edges de x al graf."""
        return self._out[self._nodes[x]].__iter__()
    #Per exercici avaluable
    def cicles(self):
        triple_cycles = []
        visited = set()
        for n1 in self._out:
            connected_nodes =self._out[n1].keys() - visited
            for n2 in connected_nodes:
                triple_cycle = connected_nodes.intersection(self._out[n2].keys())
                for n3 in triple_cycle:
                    triple_cycles.append([n1,n2,n3])
            visited += n1
        return triple_cycles
    
    def __str__(self):
        cad="===============GRAF===================\n"
     
        for it in self._out.items():
            cad1="__________________________________________________________________________________\n"
            cad1=cad1+str(it[0])+" : "
            for valor in it[1].items():
                cad1=cad1+str(str(valor[0])+"("+ str(valor[1])+" , ")
                            
            cad = cad + cad1 + "\n"
        
        return cad
    
