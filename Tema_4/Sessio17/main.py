def testDijkstra():   
    
    grade=0
    correcte=True
    print("Comment :=>> ")
    print("Comment :=>> ")
    print("Comment :=>> ============================================")
    print("Comment :=>> INICI TEST DIJKSTRA                       ==")
    print("Comment :=>> ============================================")
    
    
    print("Comment :=>> ")
    print("Comment :=>> ============================================")
    print("Comment :=>> TEST DIJKSTRA NODES x b d g e z           ==")
    print("Comment :=>> ============================================")
    nomsNodes = [ "x", "b", "d", "g", "e", "z"]
    arestes = [ [ "x","b" ],[ "x","d" ], [ "b","d" ],[ "b","g" ],["d","g"],["d","e"],[ "g","e" ],[ "g","z" ],["e","z"]]
    pesos = [4,2,1,5,8,10,2,6,2]
    print("Comment :=>> ============================================")
    print("Comment :=>> TEST CALCUL DIJKSTRA NODES x b d g e z    ==")
    print("Comment :=>> ============================================")
    gDijkstraPonderat=GrafHash.GrafHash(nomsNodes, arestes,pesos, False)
	
    anteriorNodesRes={'b': 'd', 'd': 'x', 'g': 'b', 'e': 'g', 'z': 'e'}
    distNodesRes={'x': 0, 'b': 3, 'd': 2, 'g': 8, 'e': 10, 'z': 12}
    
    distNodes,anteriorNodes =	gDijkstraPonderat.dijkstra("x")
   
    
    print("Comment :=>> ============================================")
    print("Comment :=>> ==VALIDANT DIJKSTRA NODES x b d g e z     ==")
    print("Comment :=>> ============================================")
    if (anteriorNodesRes == anteriorNodes):
            print("Comment :=>> CORRECTE RESULTAT DIJKSTRA CALCUL ANTERIOR")    
            print("Comment :=>> ", anteriorNodes)
            grade+=2
    else:
            print("Comment :=>> ERROR RESULTAT DIJKSTRA CALCUL ANTERIOR")    
            print("Comment :=>> RESULTAT DONAT", anteriorNodes)
            print("Comment :=>> RESULTAT ESPERAT:", anteriorNodesRes)
            correcte=False
            
    if (distNodesRes == distNodes):
            print("Comment :=>> CORRECTE RESULTAT DIJKSTRA CALCUL DISTANCIA")    
            print("Comment :=>> ", distNodes)
            grade+=2
    else:
            print("Comment :=>> ERROR RESULTAT DIJKSTRA CALCUL DISTANCIA")    
            print("Comment :=>> RESULTAT DONAT", distNodes)
            print("Comment :=>> RESULTAT ESPERAT:", distNodesRes)
            correcte=False
    

    print("Comment :=>> ==================================================================")
    print("Comment :=>> TEST CALCUL MINDISTANCE DIJKSTRA MODIFICAT NODES x b d g e z    ==")
    print("Comment :=>> ==================================================================")
     
    camiNodes=gDijkstraPonderat.camiMesCurt('x', 'z')
    camiNodesRes=['x', 'd', 'b', 'g', 'e', 'z']
    if (camiNodesRes == camiNodes):
            print("Comment :=>> CORRECTE RESULTAT DIJKSTRA CALCUL CAMI MINIM")    
            print("Comment :=>> ", camiNodes)
            grade+=1
    else:
            print("Comment :=>> ERROR RESULTAT DIJKSTRA CALCUL CAMI MINIM")    
            print("Comment :=>> RESULTAT DONAT", camiNodes)
            print("Comment :=>> RESULTAT ESPERAT:", camiNodesRes)
            correcte=False
  
       
    print("Comment :=>> ============================================")        
    print("Comment :=>> FINAL test DIJKSTRA NODES x b d g e z    ===")
    print("Comment :=>> ============================================")        
    
    
    #Cami mes Curt
    
    noms_nodesMetro = ["Pl. Sants","Hostafr.","Esp.","Roc.","Urgell","Univ.","Cat.","Urq.","Triomf","Marina","Glòries","Clot","Navas","Sagrera",
				 "Paral·lel","St. Ant.","Pg. Gràcia","Tetuan","Monumental","S. Família","Encants","Bac Roda","Sant Martí","La Pau",
		         "Sants Est.","Tarragona","Poble Sec","Drassanes","Liceu","Diagonal",
				  "Besòs","Besòs Mar","El Maresme","Selva Mar","Poblenou","Llacuna","Bogatell","Ciutadella","Barcelone.","Jaume I","Girona","Verdaguer","Joanic","Alfons X",
		          "Guinardó","Maragall","Llucmajor","Via Júlia",
		          "Entença","H. Clínic","Sant Pau","Camp Arpa","Congrés"]

    parells_parades = [['Pl. Sants', 'Hostafr.'],['Hostafr.', 'Esp.'],['Esp.', 'Roc.'],['Roc.', 'Urgell'],['Urgell', 'Univ.'],['Univ.', 'Cat.'],['Cat.', 'Urq.'],['Urq.', 'Triomf'],
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
    gMetro=GrafHash.GrafHash(noms_nodesMetro,parells_parades,pesosMetro,False)
    
    distMetro,anteriorMetro=gMetro.dijkstra("Pl. Sants")
    
    distResMetro={'Pl. Sants': 0, 'Hostafr.': 511, 'Esp.': 1506, 'Roc.': 1931, 'Urgell': 4202, 'Univ.': 4882, 'Cat.': 5276, 'Urq.': 5115, 'Triomf': 6718, 'Marina': 7211, 'Glòries': 8171, 'Clot': 7273, 'Navas': 7772, 'Sagrera': 8953, 'Paral·lel': 3741, 'St. Ant.': 4388, 'Pg. Gràcia': 4834, 'Tetuan': 6628, 'Monumental': 5717, 'S. Família': 5181, 'Encants': 6962, 'Bac Roda': 7981, 'Sant Martí': 8167, 'La Pau': 9049, 'Sants Est.': 113, 'Tarragona': 1909, 'Poble Sec': 2596, 'Drassanes': 6134, 'Liceu': 5896, 'Diagonal': 3180, 'Besòs': 9755, 'Besòs Mar': 10047, 'El Maresme': 10352, 'Selva Mar': 11037, 'Poblenou': 10420, 'Llacuna': 10400, 'Bogatell': 9158, 'Ciutadella': 8974, 'Barcelone.': 8319, 'Jaume I': 6285, 'Girona': 5813, 'Verdaguer': 4519, 'Joanic': 5509, 'Alfons X': 5970, 'Guinardó': 7672, 'Maragall': 8696, 'Llucmajor': 9682, 'Via Júlia': 10329, 'Entença': 1698, 'H. Clínic': 2218, 'Sant Pau': 6032, 'Camp Arpa': 7727, 'Congrés': 9575}
    antResMetro={'Hostafr.': 'Pl. Sants', 'Sants Est.': 'Pl. Sants', 'Tarragona': 'Sants Est.', 'Entença': 'Sants Est.', 'Esp.': 'Hostafr.', 'Roc.': 'Esp.', 'Poble Sec': 'Esp.', 'H. Clínic': 'Entença', 'Urgell': 'Roc.', 'Diagonal': 'H. Clínic', 'Paral·lel': 'Poble Sec', 'Pg. Gràcia': 'Diagonal', 'Verdaguer': 'Diagonal', 'St. Ant.': 'Paral·lel', 'Drassanes': 'Paral·lel', 'Univ.': 'St. Ant.', 'Girona': 'Pg. Gràcia', 'Joanic': 'Verdaguer', 'S. Família': 'Verdaguer', 'Tetuan': 'Pg. Gràcia', 'Cat.': 'Pg. Gràcia', 'Urq.': 'Pg. Gràcia', 'Triomf': 'Urq.', 'Jaume I': 'Urq.', 'Monumental': 'S. Família', 'Encants': 'S. Família', 'Sant Pau': 'S. Família', 'Liceu': 'Cat.', 'Alfons X': 'Joanic', 'Guinardó': 'Alfons X', 'Camp Arpa': 'Sant Pau', 'Barcelone.': 'Jaume I', 'Marina': 'Triomf', 'Clot': 'Encants', 'Glòries': 'Marina', 'Navas': 'Clot', 'Bac Roda': 'Clot', 'Maragall': 'Guinardó', 'Sagrera': 'Navas', 'Sant Martí': 'Bac Roda', 'La Pau': 'Sant Martí', 'Ciutadella': 'Barcelone.', 'Llucmajor': 'Maragall', 'Congrés': 'Sagrera', 'Bogatell': 'Ciutadella', 'Besòs': 'La Pau', 'Llacuna': 'Bogatell', 'Via Júlia': 'Llucmajor', 'Besòs Mar': 'Besòs', 'El Maresme': 'Besòs Mar', 'Selva Mar': 'Poblenou', 'Poblenou': 'Llacuna'}
    
    print("Comment :=>> ============================================")
    print("Comment :=>> ==VALIDANT DIJKSTRA NODES Metro           ==")
    print("Comment :=>> ============================================")
    if (antResMetro == anteriorMetro):
            print("Comment :=>> CORRECTE RESULTAT DIJKSTRA CALCUL ANTERIOR")    
            print("Comment :=>> ", anteriorMetro)
            grade+=2
    else:
            print("Comment :=>> ERROR RESULTAT DIJKSTRA CALCUL ANTERIOR")    
            print("Comment :=>> RESULTAT DONAT", anteriorMetro)
            print("Comment :=>> RESULTAT ESPERAT:", antResMetro)
            correcte=False
            
    if (distResMetro == distMetro):
            print("Comment :=>> CORRECTE RESULTAT DIJKSTRA CALCUL DISTANCIA")    
            print("Comment :=>> ", distMetro)
            grade+=2
    else:
            print("Comment :=>> ERROR RESULTAT DIJKSTRA CALCUL DISTANCIA")    
            print("Comment :=>> RESULTAT DONAT", distMetro)
            print("Comment :=>> RESULTAT ESPERAT:", distResMetro)
            correcte=False

    print("Comment :=>> ======================================================")
    print("Comment :=>> TEST CALCUL MINDISTANCE DIJKSTRA MODIFICAT Metro    ==")
    print("Comment :=>> ======================================================")
     
    camiMetro=gMetro.camiMesCurt('Sants Est.', 'Univ.')
    camiMetroRes=['Sants Est.', 'Entença', 'H. Clínic', 'Diagonal', 'Pg. Gràcia', 'Univ.']
    if (camiMetroRes == camiMetro):
            print("Comment :=>> CORRECTE RESULTAT DIJKSTRA CALCUL CAMI MINIM")    
            print("Comment :=>> ", camiMetro)
            grade+=1
    else:
            print("Comment :=>> ERROR RESULTAT DIJKSTRA CALCUL CAMI MINIM")    
            print("Comment :=>> RESULTAT DONAT", camiMetro)
            print("Comment :=>> RESULTAT ESPERAT:", camiMetroRes)
            correcte=False
  
        
    print("Comment :=>> ============================================")        
    print("Comment :=>> FINAL test DIJKSTR NODES Metro           ===")
    print("Comment :=>> ============================================")       

        
    return gDijkstraPonderat,gMetro, grade, correcte

if __name__ == "__main__":

    import GrafHash
    
    grade =0.0
    correcte=True
    
    gDijkstraPonderat,gMetro, grade, correcte = testDijkstra()
    
    if (grade >= 10):        
        grade=10
    
    if correcte:
        print("Comment :=>> ============================================")
        print("Comment :=>> FINAL DEL TEST SENSE ERRORS              ===" )
        print("Comment :=>> ============================================")

    print("Grade :=>> ",grade)
    