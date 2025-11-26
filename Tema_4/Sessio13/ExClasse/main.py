if __name__ == "__main__":

    import GrafMatriu
    
    grade =0.0
    print("Comment :=>> =====PROVES GRAF MATRIU ============================")
    
    nomsPaginesWeb = [ "pg. principal","escola","estudis","info. academica","e. graus","grau e. inf.","calendari","pla estudis","guies docents","professorat","horaris","horaris inf."]
	
	    
    print("Comment :=>> =================CREANT GRAF AMB MATRIU ADJACENCIA================" )
    g=GrafMatriu.GrafMatriu(nomsPaginesWeb)
    grade += 1
    
    
    
    RelacionsPagWeb =[[0,1],[0,2],[0,3],[0,5],[2,4],[3,6],[3,10],[4,2],[4,5],[5,6],[5,7],[5,10],[7,8],[8,9],[10,11]]
	
    print("Comment :=>> =================INSERINT EDGES AL GRAF AMB MATRIU ADJACENCIA================" )
    for p in RelacionsPagWeb :
        g.insert_edge(p[0],p[1])
    
    grade+=1
    
    print("Comment :=>> =================VERIFICANT EDGES AL GRAF AMB MATRIU ADJACENCIA================" )            
    for p in RelacionsPagWeb :
        if g.getMatrix()[p[0]][p[1]]!=1 or g.getMatrix()[p[1]][p[0]]!=1:
            print("Comment :=>> ERROR, els nodes ( " , p[0], "; ", p[1],") haurien d'estar connectats en els dos sentits i no ho estan")
        else:
            grade += 0.4

    g.insert_vertex("PAGINA NOVA")
    g.insert_edge(0,12)
    
    if g.getMatrix()[0][12]!=1:
        print("Comment :=>> ERROR, els nodes ( 0,12) haurien d'estar connectats i no ho estan")
    else:
        grade += 1
    
    if g.getMatrix()[12][0]!=1:
        print("Comment :=>> ERROR, els nodes ( 12,0) haurien d'estar connectats i no ho estan")
    else:
        grade += 1
    
    print("Comment :=>> AQUEST ES EL GRAF FINAL")
    print("Comment :=>>",g)

    if (grade >= 10):
        grade=10
        print("Comment :=>> Final del test sense errors" )

    print("Grade :=>> ",grade)