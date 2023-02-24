from math import inf
def remplirMatriceNonOrinte():

    n = int(input("Veuillez entrer le nombre de sommets de votre graphe, s'i ous plaît: \n"))

    # Initalzat de la matrice de poids M
    M = [[inf] * (n) for i in range(n)]

    print("Inisialisation de la matrice de poids: \n")

    for i in range(len(M)):
        j = i+1
        while j < (len(M)):
            print(
                "\n-------> S'il n'existe pas une arrête entre les 2 sommets tapez inf ou INF\n")
            e = input("Donnez le poids entre les sommets " +
                    str(i+1) + " et " + str(j+1)+": ")
            if e == "inf" or e == "INF":
                M[i][j] = inf
            else:
                M[i][j] = int(e)

            j += 1

    for i in range(len(M)):
        for j in range(len(M)):
            M[j][i] = M[i][j]

    print("\nvotre matrice de poids est : ")
    for i in range(n):
        print((i + 1), "=", M[i])
    return M    

def remplirMatriceOriente():
    n = int(input("donnez le nombre de sommets : \n"))

    # Matrice de poids M
    M = [[inf] * (n) for i in range(n)]
    for i in range(n):
        for j in range(n):
            e = input(
                "\ndonnez l'élément[" + str(i + 1) +
                "][" + str(j + 1) + "] de la matrice "
            )
            if e == "0":
                M[i][j] = inf
            else:
                M[i][j] = int(e)

    for i in range(n):
        for j in range(n):
            M[i][i] = 0

    # print("\n")
    print("\nvotre matrice de poids est : ")
    for i in range(n):
        print((i + 1), "=", M[i])
    return M

def remlplirprOrd() :
    n = int(input("donnez le nombre de sommets : \n"))

    # Matrice de poids M
    print("vous allez introduire votre matrice de poids\n")
    M = [[inf] * (n) for i in range(n)]
    print("Inisialisation de la matrice de poids \n")
    print("M=", M)
    for i in range(n):
        for j in range(n):
            e = input(
                "\ndonnez l'élément[" + str(i + 1) +
                "][" + str(j + 1) + "] de la matrice "
            )
            if e == "inf" or e == "INF":
                M[i][j] = inf
            else:
                M[i][j] = int(e)

    for i in range(n):
        for j in range(n):
            M[i][i] = 0

    # print("\n")
    print("\nvotre matrice de poids est : ")
    for i in range(n):
        print((i + 1), "=", M[i])

    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] != inf:
                M[i][j] = (-1)*M[i][j]

    return M