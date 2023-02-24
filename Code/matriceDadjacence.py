from math import inf 

def matriceDadjacence(M):
    MD= [[inf] * (len(M)) for i in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] == inf:
                MD[i][j] = 0
            else:
                MD[i][j] = 1

    for i in range(len(M)):
        MD[i][i] = 0
    return MD 

def display(MV, weighted):
    if weighted == True:
        for i in range(len(MV)):
            print((i + 1), "=", MV[i])

    else:
        print("\n la matrice d'adjacence de votre graphe:\n")
        MD = matriceDadjacence(MV)
        for i in range(len(MD)):
            print((i + 1), "=", MD[i])
