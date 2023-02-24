from math import inf

def djikstra(Matrice):
    Distance = [inf]*len(Matrice)
    Distance[0] = 0

    for i in range(len(Matrice)-1):
        for j in range(len(Matrice)):
            for k in range(len(Matrice)):
                if Distance[j] + Matrice[j][k] < Distance[k]:
                    Distance[k] = Distance[j] + Matrice[j][k]

    return Distance