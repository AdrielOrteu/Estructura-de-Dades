if __name__ == "__main__":

    import GrafHash
    
    grade =0.0
    print("Comment :=>> =====PROVES GRAF MATRIU ============================")
    
    nodesMetro = ["Pl. Sants","Hostafr.","Esp.","Roc.","Urgell","Univ.","Cat.","Urq.","Triomf","Marina","Glòries","Clot","Navas","Sagrera",
				 "Paral·lel","St. Ant.","Pg. Gràcia","Tetuan","Monumental","S. Família","Encants","Bac Roda","Sant Martí","La Pau",
		         "Sants Est.","Tarragona","Poble Sec","Drassanes","Liceu","Diagonal",
				  "Besòs","Besòs Mar","El Maresme","Selva Mar","Poblenou","Llacuna","Bogatell","Ciutadella","Barcelone.","Jaume I","Girona","Verdaguer","Joanic","Alfons X",
		          "Guinardó","Maragall","Llucmajor","Via Júlia",
		          "Entença","H. Clínic","Sant Pau","Camp Arpa","Congrés"]

    relacionsMetro = [['Pl. Sants', 'Hostafr.'],['Hostafr.', 'Esp.'],['Esp.', 'Roc.'],['Roc.', 'Urgell'],['Urgell', 'Univ.'],['Univ.', 'Cat.'],['Cat.', 'Urq.'],['Urq.', 'Triomf'],
                       ['Triomf', 'Marina'],['Marina', 'Glòries'],['Glòries', 'Clot'],['Clot', 'Navas'],['Navas', 'Sagrera'],['Paral·lel', 'St. Ant.'],['St. Ant.', 'Univ.'],
                       ['Univ.', 'Pg. Gràcia'],['Pg. Gràcia', 'Tetuan'],['Tetuan', 'Monumental'],['Monumental', 'S. Família'],['S. Família', 'Encants'],['Encants', 'Clot'],
                       ['Clot', 'Bac Roda'],['Bac Roda', 'Sant Martí'],['Sant Martí', 'La Pau'],['Sants Est.', 'Tarragona'],['Tarragona', 'Esp.'],['Esp.', 'Poble Sec'],
                       ['Poble Sec', 'Paral·lel'],['Paral·lel', 'Drassanes'],['Drassanes', 'Liceu'],['Liceu', 'Cat.'],['Cat.', 'Pg. Gràcia'],['Pg. Gràcia', 'Diagonal'],
                       ['La Pau', 'Besòs'],['Besòs', 'Besòs Mar'],['Besòs Mar', 'El Maresme'],['El Maresme', 'Selva Mar'],['Selva Mar', 'Poblenou'],['Poblenou', 'Llacuna'],
                       ['Llacuna', 'Bogatell'],['Bogatell', 'Ciutadella'],['Ciutadella', 'Barcelone.'],['Barcelone.', 'Jaume I'],['Jaume I', 'Urq.'],['Urq.', 'Pg. Gràcia'],
                       ['Pg. Gràcia', 'Girona'],['Girona', 'Verdaguer'],['Verdaguer', 'Joanic'],['Joanic', 'Alfons X'],['Alfons X', 'Guinardó'],['Guinardó', 'Maragall'],
                       ['Maragall', 'Llucmajor'],['Llucmajor', 'Via Júlia'],['Pl. Sants', 'Sants Est.'],['Sants Est.', 'Entença'],['Entença', 'H. Clínic'],['H. Clínic', 'Diagonal'],
                       ['Diagonal', 'Verdaguer'],['Verdaguer', 'S. Família'],['S. Família', 'Sant Pau'],['Sant Pau', 'Camp Arpa'],['Camp Arpa', 'Sagrera'],['Sagrera', 'Congrés'],
                       ['Congrés', 'Maragall']]
    pesosMetro = [511,995,425,2271,1782,787,375,1603,493,960,1212,499,1181,647,494,124,1794,1607,536,1781,311,708,186,882,1796,1132,1090,1145,2393,1730,620,442,1654,706,292,305,1204,
             617,20,1242,184,655,2034,1170,281,979,1569,990,461,1702,1024,986,647,113,1585,520,962,1339,662,851,1695,1337,622,1290 ]

    g=GrafHash.GrafHash(nodesMetro,relacionsMetro,pesosMetro)
    
    grade += 2
    
    
    print("Comment :=>> VERIFICATN PES EDGE      ")
    if g.getOut()['Congrés']['Maragall']==pesosMetro[-1]:
        print("Comment :=>> CORRECTE PES CORRECTE:      ", pesosMetro[-1])
        grade+=2
    else:
        print("Comment :=>> ERROR PES INCORRECTE: Has donat: ",g.getOut()['Congrés']['Maragall']," I HAURIA DE SER: ",  pesosMetro[-1])
    
    print("Comment :=>> ITERANT SOBRE ELS VERTEXS      ")
    lvertexs=[]
    for n in g.vertices():
        lvertexs.append(n)
        print(n)

    if set(lvertexs)==set(nodesMetro):
        print("Comment :=>> CORRECTE, Vertexs iterats correctament")
        grade+=3
    else:
        print("Comment :=>> ERROR, Vertexs NO iterats correctament")
    
    print("Comment :=>> ITERANT SOBRE ELS EDGES      ")
    
    lResEdges=[set(['Cat.', 'Univ.']),set(['Cat.', 'Urq.']),set(['Cat.', 'Pg. Gràcia']),set(['Cat.', 'Liceu'])]
    ledges=[]
    for v in g.edges('Cat.'):
        ledges.append(set(['Cat.',v]))
        print('Cat.',v)

    correcte=len(lResEdges)==len(ledges)
    if correcte:
        print("Comment :=>> CORRECTE LONGITUD")
        grade+=1
        for p in lResEdges:
            if not set(p) in ledges:
                correcte=False
                print("Comment :=>> ERROR NO TROBA",p)
                break
       
    if correcte:
        print("Comment :=>> CORRECTE, Edges de 6 iterats correctament")
        grade+=2
    else:
        print("Comment :=>> ERROR, Edges de 6 NO iterats correctament")
        
    print("Comment :=>> AQUEST ES EL GRAF FINAL")
    print("Comment :=>>",g)

    if (grade >= 10):
        grade=10
        print("Comment :=>> Final del test sense errors" )

    print("Grade :=>> ",grade)