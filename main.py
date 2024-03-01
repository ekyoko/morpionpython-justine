
#1/ affiche les numéros de colonnes, de 1 à la taille de la grille
#2/ itère sur chaque ligne de la grille et affiche le contenu
#3/ affiche des | pour séparer les colonnes et des - pour séparer les lignes
def afficher_grille(grille):
    longueur = len(grille)
    print(". |", " | ".join(str(i) for i in range(1, longueur + 1)) + " | ")
    print(" " + "-" * (4 * longueur +1))
    for i, ligne in enumerate(grille, start=1):   #enumere chaque element de la liste grille et renvoyer une paire de valeur qui contient l'élément et son indice
        print(str(i) + " |", " | ".join(ligne) + " | ")
        print(" " + "-" * (4 * longueur + 1))

def creer_grille(taille):
    return [[" " for _ in range(taille)] for _ in range(taille)]

def morpion():
    taille = int(input("Entrez la taille de la grille (minimum 3) : "))
    while taille < 3:   #utilisation de while afin de pouvoir ressayer indéfiniment si la perosnne se trompe
        print("Abuse un morpion c'est 3 mini.")
        taille = int(input("Entrez la taille de la grille : "))
    grille = creer_grille(taille)
    afficher_grille(grille)

morpion()