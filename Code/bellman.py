from math import inf

def Bellman(Matrice):
    Distance = [inf]*len(Matrice)
    Distance[0] = 0

    for i in range(len(Matrice)-1):
        for j in range(len(Matrice)):
            for k in range(len(Matrice)):
                if Distance[j] + Matrice[j][k] < Distance[k]:
                    Distance[k] = Distance[j] + Matrice[j][k]

    for i in range(len(Matrice)):
        for j in range(len(Matrice)):
            if Distance[i] + Matrice[i][j] < Distance[j]:
                print("Le graphe contient un cycle négatif")
                return

    return Distance



