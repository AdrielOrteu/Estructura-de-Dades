import copy

class GrafMatriu:
    """Graf de Adjacency Map structure"""
 
################################Definicio Class GrafMatriu       
    def __init__(self, ln=[]):
        """Create a graph without connections"""
        n = len(ln)
        self._matriuAdj = [ [0] * n for j in range(n) ]
        self._nodes = copy.deepcopy(ln)
        self._size = n
    
    def insert_vertex(self, x=None):
        """Insert and return a new Vertex with element x"""
        self._nodes.append(x)
        self._size += 1
        for l in self._matriuAdj:
            l.append(0)
        self._matriuAdj.append([0]*self._size)
        

    def insert_edge(self, u, v):
        """Insert a new Edge from u to v and from v to u"""
        if v < self._size and u < self._size:
            self._matriuAdj[u][v] = 1
            self._matriuAdj[v][u] = 1
    
    def getMatrix(self):            
        return self._matriuAdj
    
    def __str__(self):
        cad=""
        for v in self._nodes:
            cad=cad+str(v)+" "
        cad=cad+"\n"
        
        for l in self._matriuAdj:
            for v in l:
                cad=cad+str(v)+" "
            cad=cad+"\n"
        return cad
    
