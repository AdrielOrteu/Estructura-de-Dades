def testGrafTasquesRecorregutDFS(grade,correcte):
    print("Comment :=>> ============================================")
    print("Comment :=>> INICI testGrafTasquesRecorregutDFS        ==")
    print("Comment :=>> ============================================")
    nodes_Tasques2=["T1","T2","T3","T4","T5","T6","T7","T8","T9","T10","T11"]         
    relacionsTasques2=[["T1","T2"],["T1","T3"],["T1","T4"],["T2","T5"],["T2","T6"],
                      ["T3","T2"],["T3","T4"],["T4","T6"],["T4","T7"],
                      ["T5","T8"],["T5","T9"],["T6","T5"],["T6","T7"],
                      ["T7","T9"],["T7","T10"],
                      ["T8","T9"],["T8","T11"],["T9","T10"],["T9","T11"],["T10","T11"]]
    pesosTasques2=[5,5,5,10,10,7,7,4,4,3,3,6,6,9,9,1,2,8,8,4]
    nodeIniFi=[["T1","T11"],["T2","T11"]]
    g4=GrafHash.GrafHash(nodes_Tasques2,relacionsTasques2,pesosTasques2,True)
    resRecorregutsDFS=[['T1', 'T2', 'T5', 'T8', 'T9', 'T10', 'T11', 'T6', 'T7', 'T3', 'T4'],['T2', 'T5', 'T8', 'T9', 'T10', 'T11', 'T6', 'T7']]
    
    print("Comment :=>> ============================================")
    print("Comment :=>> CALCULANT DFS                             ==")
    print("Comment :=>> ============================================")
    for i in range(len(nodeIniFi)):
        visitat, recorregut = g4.DFS(nodeIniFi[i][0])
        if (recorregut == resRecorregutsDFS[i]):
            print("Comment :=>> CORRECTE RESULTAT RECORREGUT DFS A PARTIR DE", nodeIniFi[i][0], " FINS A : ", nodeIniFi[i][1])    
            print("Comment :=>> ", recorregut)
            grade+=2.5
        else:
            print("Comment :=>> ERROR RESULTAT RECORREGUT DFS A PARTIR DE", nodeIniFi[i][0], " FINS A : ", nodeIniFi[i][1])    
            print("Comment :=>> RESULTAT DONAT", recorregut)
            print("Comment :=>> RESULTAT ESPERAT:", resRecorregutsDFS[i])
                                
    print("Comment :=>> ============================================")    
    print("Comment :=>> FINAL testGrafTasquesRecorregutDFS        ==")
    print("Comment :=>> ============================================")

    return grade,correcte,g4,visitat,recorregut
   
def testGrafLApersona(grade,correcte):
    print("Comment :=>> ")
    print("Comment :=>> ")
    print("Comment :=>> ============================================")
    print("Comment :=>> INICI testGrafLApersona                   ==")
    print("Comment :=>> ============================================")
    nodes_LAPERSONA=["Tu","Marta","Maria","Jordi","Berta","Aritz","Nikita",
                     "Joshua","Marc","Mar","Umair","Neus","LA persona"]
    relacions_LAPERSONA=[["Tu","Maria"],["Tu","Jordi"],["Tu","Marc"],
                     ["Maria","Marta"],["Maria","Jordi"],["Maria","Aritz"],
                     ["Jordi","Berta"],
                     ["Berta","Nikita"],["Berta","Joshua"],
                     ["Aritz","Nikita"],
                     ["Joshua","LA persona"],
                     ["Marc","Mar"],["Marc","Umair"],
                     ["Umair","Neus"],["Umair","LA persona"]]
    pesosLAPERSONA=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    resVisitatLaPersona={'Tu': None, 'Maria': 'Tu', 'Jordi': 'Tu', 'Marc': 'Tu', 'Marta': 'Maria', 'Aritz': 'Maria', 'Berta': 'Jordi', 'Mar': 'Marc', 'Umair': 'Marc', 'Nikita': 'Aritz', 'Joshua': 'Berta', 'Neus': 'Umair', 'LA persona': 'Umair'}
    
    print("Comment :=>> ============================================")
    print("Comment :=>> ==CREANT GRAF LA PERSONA                  ==")
    print("Comment :=>> ============================================")
    
    g5 = GrafHash.GrafHash(nodes_LAPERSONA,relacions_LAPERSONA,pesosLAPERSONA,True)
    
    print("Comment :=>> ============================================")
    print("Comment :=>> ==CALCULANT BFS                           ==")
    print("Comment :=>> ============================================")
    visitatLApersona = g5.BFS("Tu")
       
    print("Comment :=>> ============================================")
    print("Comment :=>> ==VALIDANT BFS                            ==")
    print("Comment :=>> ============================================")
    if (visitatLApersona == resVisitatLaPersona):
            print("Comment :=>> CORRECTE RESULTAT PATH DE Tu A LA persona")    
            print("Comment :=>> ", visitatLApersona)
            grade+=5
    else:
            print("Comment :=>> ERROR RESULTAT PATH DE Tu A LA persona")    
            print("Comment :=>> RESULTAT DONAT", visitatLApersona)
            print("Comment :=>> RESULTAT ESPERAT:", resVisitatLaPersona)
    print("Comment :=>> ============================================")        
    print("Comment :=>> FINAL testGrafLApersona                  ===")
    print("Comment :=>> ============================================")        
    return grade,correcte,g5,visitatLApersona

if __name__ == "__main__":

    import GrafHash
    
    grade =0.0
    correcte=True
    
    grade,correcte,g4,visitat,recorregut=testGrafTasquesRecorregutDFS(grade,correcte)
    
    grade,correcte,g5,visitatLApersona=testGrafLApersona(grade,correcte)  
    
    if (grade >= 10):        
        grade=10
    
    if correcte:
        print("Comment :=>> ============================================")
        print("Comment :=>> FINAL DEL TEST SENSE ERRORS              ===" )
        print("Comment :=>> ============================================")

    print("Grade :=>> ",grade)
    