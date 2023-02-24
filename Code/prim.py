from math import inf

#Vérifier si la matrice de l'arbre couvrant de poids contient tous les sommets de la matrice de poids
def fullNodesList(nodesList):
    for i in nodesList:
        if i == False:
            return False
    return True

#Ajouter un noeud à l'arbre couvrant de poids
def addNode(M, nodesList, MAC):
    min = inf
    for i in range(0,len(M)):
        if(nodesList[i]==True):
            for j in range(0,len(M)):
                if(nodesList[j]==False and min >M[i][j]):
                    mini = i
                    minj = j
                    min = M[i][j]    
    MAC[mini][minj] = M[mini][minj]
    MAC[minj][mini] = M[mini][minj]
    nodesList[minj] = True

#Fonction prim
def prim(M):

    # Initializer la matrice de l'arbre couvrant de poids
    MAC = [[inf] * (len(M)) for i in range(len(M))]
    # Tableau de sommet de MAC
    nodesList = [False] * (len(M))

    #Ajouter le sommet "0" à l'arbre couvrant de poinds
    nodesList[0] = True
    while(fullNodesList(nodesList) == False):
        addNode(M, nodesList, MAC)
    return(MAC)

#test
#M = remplirMatrice.remplirMatrice()
#print(prim(M))

    










