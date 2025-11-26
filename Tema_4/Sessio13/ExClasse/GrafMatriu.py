import copy

class GrafMatriu:
    """Graf de Adjacency Map structure"""
 
################################Definicio Class GrafMatriu       
    def __init__(self, ln=[], par=[], w=[]): # par -> llista de parelles de nodes (arestes) | w -> llista de pesos corresponents a les parelles de par (en el mateix ordre)
        """ EXERCICIS 1 i 2 """

        """Create a graph withous connections"""
        self._nodes = copy.deepcopy(ln)
        self._numNodes = len(ln)
        self._matriuAdj = [ [0] *self._numNodes for j in range(self._numNodes) ]      
        self._numEdges = 0
        self._ponderat = 0
        
        if w:
            self._ponderat = 1
            
        k = len(par) - len(w)
        w.extend([1]*k)
        for nodes, weigth in zip(par, w):
            indu = self._nodes.index(nodes[0])
            indv = self._nodes.index(nodes[1])
            self.insert_edge(indu, indv, weigth)
    
    def getMatrix(self):            
        return self._matriuAdj
    
    def insert_vertex(self, x=None):
        """Insert and return a new Vertex with element x"""
        self._nodes.append(x)
           
        for j in range(self._numNodes):
            self._matriuAdj[j].append(0)
        self._numNodes+=1
        self._matriuAdj.append( [0] *self._numNodes)

    def insert_edge(self, u, v, w=1): # Assignem un pes d'1 perdefecte
        """Insert a new Edge from u to v and from v to u"""
        if (0<=u<self._numNodes) and (0<=v<self._numNodes):
            if (self._matriuAdj[u][v] == 0):
                self._numEdges+=1
            # NOTE: Modifiquem el valor que s'assigna d'1 (hi ha aresta) a w (el pes d'aquesta aresta)
            self._matriuAdj[u][v] = w 
            self._matriuAdj[v][u] = w
            
    def vertices(self):
        """ EXERCICI 3 """
        return self._nodes.__iter__()
        
    def edges(self, v):
        """ EXERCICI 3 """
        for col in range(0, self._numNodes):
            if self._matriuAdj[v][col] != 0:
                yield (self._nodes[v],self._nodes[col])
        
    def cicles(self):
        """ EXERCICI 4 """
        cicles = []
        for i in range(self._numNodes): # i -> fila
            for j in range(i+1, self._numNodes): # j -> columna
                if self._matriuAdj[i][j] != 0:
                    for k in range(j+1, self._numNodes): # k -> vei
                        if self._matriuAdj[i][k] != 0 and self._matriuAdj[j][k] != 0:
                            cicles.append([self._nodes[i], self._nodes[j], self._nodes[k]])
        return cicles
             
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
    
    