def Test(grade,correcte):

    print("Comment :=>> ============================================")
    print("Comment :=>> INICI DEL TEST BINARYTREE ARBRES-I       ===")
    print("Comment :=>> ============================================")

    grade = 0.0
    correcte = True
    
    resArbre=['Comment :=>> +\nComment :=>>   *\nComment :=>>     +\nComment :=>>       3\nComment :=>>       9\nComment :=>>     /\nComment :=>>       5\nComment :=>>       2\nComment :=>>   7\n',
            'Comment :=>> 35\nComment :=>>   15\nComment :=>>     10\nComment :=>>     25\nComment :=>>   80\nComment :=>>     47\nComment :=>>     92\nComment :=>>       105\n',
            'Comment :=>> 35\nComment :=>>   80\nComment :=>>     92\nComment :=>>       90\nComment :=>>       105\n']   
    nomF=["arbreOps.txt","arbreOrdenat.txt","arbreOrdenat2.txt"]

    resGermansFD=[1,1,0]
    resFills=[2,2,1]
    resGrauNode=[2,2,1]

    resPreordre=['\n+\n*\n+\n3\n9\n/\n5\n2\n7','\n35\n15\n10\n25\n80\n47\n92\n105','\n35\n80\n92\n90\n105']
    resInordre=['\n3\n+\n9\n*\n5\n/\n2\n+\n7','\n10\n15\n25\n35\n47\n80\n92\n105','\n35\n80\n90\n92\n105']


    print("Comment :=>> =====================")
    print("Comment :=>> CREANT ARBRE BUIT ===")
    print("Comment :=>> =====================")
    tbuit=BinaryTree.BinaryTree()
    print(tbuit)
    print("Comment :=>> ================================")
    print("Comment :=>> MIRANT ESBUIT DE BUIT        ===")
    print("Comment :=>> ================================")
    if tbuit.esBuit():
        print("Comment :=>> CORRECTE ARBRE BUIT ES BUIT")
        grade += 0.1            
    else:
        print("Comment :=>> ERROR HAS DIT QUE ARBRE BUIT NO ES BUIT I SI QUE HO ES")
        correcte=False 
    
    for i,nom in enumerate(nomF):
        print("Comment :=>> =====================")
        print("Comment :=>> CREANT ARBRE      ===")
        print("Comment :=>> =====================")
        t=BinaryTree.BinaryTree()
        t.read(nom)
        print(t)
        cad=str(t)
        if (cad==resArbre[i]):
            print("Comment :=>> ARBRE CREAT CORRECTAMENT")    
            print("Comment :=>> ARBRE \n", t)        
        else:
            print("Comment :=>> ARBRE CREAT INCORRECTAMENT")    
            print("Comment :=>> RESULTAT DONAT ", cad)
            print("Comment :=>> RESULTAT ESPERAT:", resArbre[i])
            correcte=False
        
        print("Comment :=>> ================================")
        print("Comment :=>> MIRANT ESARREL, ESFULLA, BUIT===")
        print("Comment :=>> ================================")
    
        if t.esArrel():
            print("Comment :=>> CORRECTE ARBRE ES ARREL")
            grade += 0.1
        else:
            print("Comment :=>> ERROR HAS DIT QUE NO ES ARREL L'ARREL DE L'ARBRE ES ARREL")
            correcte=False
            
        if t._right.esArrel():
            print("Comment :=>> ERROR HAS DIT QUE FILLDRET ES ARREL, I NO HO ES")
            correcte=False
        else:
            print("Comment :=>> CORRECTE FILLDRET NO ES ARREL")
            grade += 0.1
        
        if not t.esFulla():
            print("Comment :=>> CORRECTE ARREL NO ES FULLA")
            grade += 0.1
        else:
            print("Comment :=>> ERROR HAS DIT QUE ARREL AMB FILLS ES FULLA")
            correcte=False
            
        
        if i==0: 
            if t._right.esFulla():
                print("Comment :=>> CORRECTE FILL DRET ES FULLA")
                grade += 0.1
            else:
                print("Comment :=>> ERROR HAS DIT FILL DRET NO ES FULLA I SI QUE HO ES")
                correcte=False
        elif i==1: 
            if t._right._right._right.esFulla():
                print("Comment :=>> CORRECTE FILL DRET_DRET_DRET ES FULLA")
                grade += 0.1
            else:
                print("Comment :=>> ERROR HAS DIT FILL DRET_DRET_DRET NO ES FULLA I SI QUE HO ES")
                correcte=False
        
        if t.esBuit():
            print("Comment :=>> ERROR HAS DIT QUE ARBRE ES BUIT I NO HO ES")
            correcte=False
        else:
            print("Comment :=>> CORRECTE ARBRE NO ES BUIT")
            grade += 0.1
        
        
        print("Comment :=>> ================================")
        print("Comment :=>> MIRANT PROFUNDITAT           ===")
        print("Comment :=>> ================================")
        
        profunditat = t.profunditat()
        if  profunditat == 0:
            print("Comment :=>> CORRECTE LA PROFUNDITAT ES", profunditat )
            grade += 0.2
        else:
            print("Comment :=>> ERROR HAS DIT QUE LA PROFUNDITAT ES", profunditat, "I EL VALOR CORRECTE ES: 0")
            correcte=False
        
        print("Comment :=>> ================================")
        print("Comment :=>> MIRANT ALÇADA                ===")
        print("Comment :=>> ================================")
        
        alcada = t.alcada()
        if  alcada == 3:
            print("Comment :=>> CORRECTE L'ALÇADA ES 3" )
            grade += 0.2
        else:
            print("Comment :=>> ERROR HAS DIT QUE L'ALÇADA ES", alcada, "I EL VALOR CORRECTE ES: 3")
            correcte=False
            
        
        print("Comment :=>> ================================")
        print("Comment :=>> MIRANT GERMANS               ===")
        print("Comment :=>> ================================")
        
        germa= t._right.germa()
        print("GERMA:",germa)
        if resGermansFD[i]== 0:
            if germa==None:
                print("Comment :=>> CORRECTE EL FD DE L'ARREL NO TE GERMANS")
                grade += 0.2
            else:
                print("Comment :=>> ERROR HAS DIT QUE EL FD DE L'ARREL TE GERMANS I NO ES CERT")
                correcte=False
                
        if resGermansFD[i]== 1:
            if germa==None:
                print("Comment :=>> ERROR HAS DIT QUE EL FD DE L'ARREL NO TE GERMANS I SI QUE TE")
                correcte=False
            else:
                print("Comment :=>> CORRECTE HAS DIT QUE EL FD DE L'ARREL TE 1 GERMA I ES CERT")
                grade += 0.2
            
        print("Comment :=>> ================================")
        print("Comment :=>> MIRANT FILLS                 ===")
        print("Comment :=>> ================================")
        correcteF = True
        for j,f in enumerate(t.fills()):
            print("FILL:", f)
            if (j>resFills[i]):
                print("Comment :=>> ERROR HAS DIT QUE L'ARREL TE MES FILLS DEL COMPTE")
                correcteF=False
        if  correcteF:
            print("Comment :=>> CORRECTE L'ARREL TE:",resFills[i], " FILLS")
            grade += 0.2      
        
        print("Comment :=>> ================================")
        print("Comment :=>> MIRANT GRAU NODE I GRAU ARBRE ==")
        print("Comment :=>> ================================")
        grauNode = t.grauNode()
        if  grauNode== resGrauNode[i]:
            print("Comment :=>> CORRECTE EL GRAU DE L'ARREL ES: ",grauNode)
            grade += 0.17
        else:
            print("Comment :=>> ERROR HAS DIT QUE EL GRAU DE L'ARREL ES: ",grauNode," , PERO ES: ", resGrauNode[i])
            correcte=False
            
        grauArbre = t.grauTree()          
        if  grauArbre== 2:
            print("Comment :=>> CORRECTE EL GRAU DE L'ARBRE ES: 2")
            grade += 0.2
        else:
            print("Comment :=>> ERROR HAS DIT QUE EL GRAU DE L'ARBRE ES: ",grauArbre," , PERO ES: 2")
            correcte=False


        print("Comment :=>> ==================")
        print("Comment :=>> MIRANT preordre===")
        print("Comment :=>> ==================")
        cadPreordre=""
        for n in t.preordre():
            #print(n._valor)
            cadPreordre += "\n" + str(n._valor)
        print(cadPreordre)   
        
        if  cadPreordre == resPreordre[i]:
            print("Comment :=>> CORRECTE EL RECORREGUT EN PREORDRE ES CORRECTE: ",cadPreordre)
            grade += 1
        else:
            print("Comment :=>> ERROR EL RECORREGUT EN PREORDRE ES INCORRECTE, Tu HAS DONAT: ",cadPreordre," , PERO ES: ", resPreordre[i])
            correcte=False
            
        print("Comment :=>> ==================")
        print("Comment :=>> MIRANT inordre ===")
        print("Comment :=>> ==================")
        
        cadInordre=""
        for n in t.inordre():
            #print(n._valor)
            cadInordre += "\n" + str(n._valor)
        print(cadInordre) 
        
        if  cadInordre == resInordre[i]:
            print("Comment :=>> CORRECTE EL RECORREGUT EN INORDRE ES CORRECTE: ",cadInordre)
            grade += 1
        else:
            print("Comment :=>> ERROR EL RECORREGUT EN INORDRE ES INCORRECTE, Tu HAS DONAT: ",cadInordre," , PERO ES: ", resInordre[i])
            correcte=False
        
        if i>0:
             print("Comment :=>> ==================")
             print("Comment :=>> CERCANT        ===")
             print("Comment :=>> ==================")
             n=t.cerca(23)
             if n==None:
                print("Comment :=>> CORRECTE EL 23 NO EXISTEIX A L'ARBRE: ")
                grade += 0.5 
             else:
                print("Comment :=>> ERROR EL 23 NO EXISTEIX A L'ARBRE I HAS DIT QUE SI: ")
                correcte=False 
                
             n2=t.cerca(105)
             if n2 is not None:
                 if n2._valor==105:
                     print("Comment :=>> CORRECTE EL 105 EXISTEIX A L'ARBRE: ")
                     grade += 1 
                 else:
                     print("Comment :=>> ERROR EL 105 EXISTEIX A L'ARBRE PERO HAS RETORNAT UN ALTRE NODE: ")
                     correcte=False 
             else:
                print("Comment :=>> ERROR EL 105 EXISTEIX A L'ARBRE I HAS DIT QUE NO: ")
                correcte=False 
                
             n3=t.cerca(1000)
             if n3==None:
                print("Comment :=>> CORRECTE EL 1000 NO EXISTEIX A L'ARBRE: ")
                grade += 0.5
             else:
                print("Comment :=>> ERROR EL 1000 NO EXISTEIX A L'ARBRE I HAS DIT QUE SI: ")
                correcte=False 

    return grade,correcte
    # --- FI TEST

if __name__ == "__main__":

    import BinaryTree
    grade = 0.0
    correcte = True

    grade,correcte = Test(grade,correcte)

    if (grade >= 10):        
        grade=10

    if correcte:
        print("Comment :=>> ============================================")
        print("Comment :=>> FINAL DEL TEST SENSE ERRORS              ===")
        print("Comment :=>> ============================================")

    print("Grade :=>> ",grade)

