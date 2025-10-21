if __name__ == "__main__":

    grade = 0
     
    import LlistaN
    
    l = [ "T0", "T1","T2","T3","T4","T5","T6","T7","T8","T9","T10", "T11"]
    resultats = [ 5,5,7,7,4,4,6,6,3,3,9,9,1,8,2,8,4 ]
    
    
   
      
    
    print ("Comment :=>> Iniciant test")
    print ("Comment :=>> =======================================================")
    
    print ("Comment :=>> =======================================================")
    print ("Comment :=>> =======    CERCA RECURSIVA                     ========")
    print ("Comment :=>> =======================================================")
    print ("Comment :=>> Inicialitzant la llista .......")
    l = LlistaN.LlistaN([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ])

    print ("Comment :=>> -----------------------------")
    print ("Comment :=>> Cerquem element existent:")
    if (l.cerca(7)):
        print ("Comment :=>> OK 7 existeix a la llista" )
        grade+=1
    else:
        print ("Comment :=>> ERROR 7 existeix a la llista i has retornat false" )

    print ("Comment :=>> -----------------------------")
    print ("Comment :=>> Cerquem 1er element existent:")
    if (l.cerca(1)):
        print ("Comment :=>> OK 1 existeix a la llista" )
        grade+=1
    else:
        print ("Comment :=>> ERROR 1 existeix a la llista i has retornat false" )
    
    print ("Comment :=>> -----------------------------")
    print ("Comment :=>> Cerquem ultim element existent:")
    if (l.cerca(10)):
        print ("Comment :=>> OK 10 existeix a la llista" )
        grade+=1
    else:
        print ("Comment :=>> ERROR 10 existeix a la llista i has retornat false" )  
        
    print ("Comment :=>> -----------------------------")
    print ("Comment :=>> Cerquem element no existent:")
    if not (l.cerca (11)):
        print ("Comment :=>> OK 11 no existeix a la llista i has retornat false" )
        grade+=1
    else:
        print ("Comment :=>> ERROR 11 no existeix a la llista i has retornat True" )
    
    print ("Comment :=>> =======================================================")
    print ("Comment :=>> =======    STRING INVERS RECURSIU              ========")
    print ("Comment :=>> =======================================================")
    print ("Comment :=>> Inicialitzant la llista .......")
    l2 = LlistaN.LlistaN(["Anna","Carles","David","Francesc","Joan","Jordi","Marc","Marta","Monica","Silvia"])
    stringInvers= "Silvia , Monica , Marta , Marc , Jordi , Joan , Francesc , David , Carles , Anna"
    invers=l2.printInvers()
    if (invers==stringInvers):
        print ("Comment :=>> OK l'string invers es correcte i es:", invers )
        grade+=3
    else:
        print ("Comment :=>> ERROR l'string invers es:", stringInvers," i tu has donat", invers)
   
    print ("Comment :=>> =======================================================")
    print ("Comment :=>> =======    STRING INVERS ITERATIU              ========")
    print ("Comment :=>> =======================================================")
    inversIter=l2.printInversIter()
    if (inversIter==stringInvers):
        print ("Comment :=>> OK l'string invers es correcte i es:", inversIter )
        grade+=3
    else:
        print ("Comment :=>> ERROR l'string invers es:", stringInvers," i tu has donat", inversIter)
   
    if (grade <0):
        grade = 0
    print ("Grade :=>>", grade)
    
    
    
    
    print ("Comment :=>> ------------------------------------------")
    if (grade == 10.0):
        print ("Comment :=>> Final del test sense errors")
    print ("Grade :=>> ", grade)
