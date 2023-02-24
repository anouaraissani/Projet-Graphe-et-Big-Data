from djikstra import djikstra
from matriceDadjacence import display
import remplirMatricePoids, prim, bellman, djikstra, remplirMatricePoids
from math import inf

x = 1
while(x == 1):
    print("\n\n___________________PROJET GBD MENU___________________________\n")
   
    print('''
                             \n  1 ==>   Display
                             \n  2 ==>   Djiksta
                             \n  3 ==>   Bellman
                             \n  4 ==>   Prim
                             \n  5 ==>   l'application d'ordonnancement
                             \n  0 ==>   sortir
    ''')
    print("\n____________________________________________________________\n\n")
    print("Veuillez choisir votre algorithme préféré s'il vous plaît: ")

    choix = input("Mon choix: ")

    if choix == '1':
        g = inf
        while(g != 0 and g != 1):
            g = input("\nVeulliez enter '0' si vous voulez un graphe orienté, '1' pour un graphe non orienté\n")
            if g == '0':
                M = remplirMatricePoids.remplirMatriceOriente()
                display(M, False)
                break
            elif g == '1':
                M = remplirMatricePoids.remplirMatriceNonOrinte()  
                display(M, False) 
                break 
            
       

    elif choix == '2':
        M = remplirMatricePoids.remplirMatriceOriente() 
        M_Dis = djikstra.djikstra(M)
        print("\nDistance depuis la source (Djiksta):\n")
        for i in range(len(M_Dis)):
            print("Sommet", (i+1), "\t------------>\t", M_Dis[i])


    elif choix == '3':
        M = remplirMatricePoids.remplirMatriceOriente() 
        M_Dis = bellman.Bellman(M)
        print("\nDistance depuis la source (Bellman):\n")

        for i in range(len(M_Dis)):
            print("Sommet", (i+1), "\t------------>\t", M_Dis[i])


    elif choix == '4':
        M = remplirMatricePoids.remplirMatriceNonOrinte()
        MAC = prim.prim(M)
        print("\nLa matrice de l'arbre couvrant de poids:\n")
        for i in range(len(MAC)):
            print((i + 1), "=", MAC[i])



    elif choix == '5':
        M = remplirMatricePoids.remlplirprOrd() 
        
        M_Dis = bellman.Bellman(M)
        print("\nDistance depuis la source (Problème d'ordonnancement) :\n")
        for i in range(len(M_Dis)):
            print("Sommet", (i+1), "\t------------>\t", (-1)*M_Dis[i])



    elif choix =='0':
        x = 0
        print("\n\n~~~~ ~~~~ ~~~~ Merci (✿ ^‿ ^) ~~~~ ~~~~ ~~~~")

        




