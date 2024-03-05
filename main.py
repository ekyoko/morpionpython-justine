import random


# On sépare les deux fonctions pour créer et afficher la grille:
# Creer_grille = generation de la structure de données
# Afficher_grille = affichage utilisateur
# On facilite aussi le debugage et on obtient une clarté dans le code

def afficher_grille(grille):
    # La fonction commence par afficher les numéros de colonnes, de 1 à la taille de la grille.
    # Ensuite, elle itère sur chaque ligne de la grille et affiche son contenu,
    # en séparant chaque élément par des barres verticales (|).
    # Entre chaque ligne, elle affiche une ligne de séparation pour rendre la grille plus lisible.

    longueur = len(grille)
    print(". |", " | ".join(str(i) for i in range(1, longueur + 1)) + " | ")
    print(" " + "-" * (4 * longueur + 1))
    for i, ligne in enumerate(grille, start=1):
        print(str(i) + " |", " | ".join(ligne) + " | ")
        print(" " + "-" * (4 * longueur + 1))


def creer_grille(taille):
    # création d'une grille de Morpion vide avec une taille spécifiée
    return [[" " for _ in range(taille)] for _ in range(taille)]


#######################################################################################################################

# Détection victoire

def detection_ligne(grille, pion):
    for ligne in grille:
        if all(case == pion for case in ligne):
            return True
    return False


def detection_colonne(grille, pion):
    taille = len(grille)
    for i in range(taille):  # Parcours des colonnes
        colonne = [grille[j][i] for j in range(taille)]  # Récupération des éléments de la colonne j
        if all(case == pion for case in colonne):  # Vérification si tous les éléments de la colonne sont égaux à pion
            return True
    return False


def detection_diagonale(grille, pion):
    taille = len(grille)

    # Diagonale HG BD
    # Parcours les éléments de la diagonale de la position 1-1 jusqu'a la posotion i-i (i=taille de la grille)
    diagonale_HGBD = [grille[i][i] for i in range(taille)]  #Stock dans une liste
    if all(case == pion for case in diagonale_HGBD):  #Vérification que tous les éléments de cette diagonale sont égaux à "pion"
        return True

    # Diagonale BG HD
    diagonale_BGHD = [grille[i][taille - i - 1] for i in range(taille)]
    if all(case == pion for case in diagonale_BGHD):
        return True

    return False


def victoire(grille, pion):
    return (detection_ligne(grille, pion) or detection_colonne(grille, pion) or detection_diagonale(grille, pion))


#######################################################################################################################

# Placer les pions de chaque joueur

def placer_pion(grille, ligne, colonne, pion):
    if grille[ligne][colonne] == " ":
        grille[ligne][colonne] = pion
        return True
    else:
        return False


def tour_joueur(grille):
    longueur = len(grille)
    while True:
        try:
            ligne = int(input("Entrez le numéro de ligne (1 à " + str(longueur) + "): ")) - 1
            colonne = int(input("Entrez le numéro de colonne (1 à " + str(longueur) + "): ")) - 1
            if 0 <= ligne < longueur and 0 <= colonne < longueur:
                if placer_pion(grille, ligne, colonne, "X"):
                    break  # le tour est terminé
                else:
                    print("Cette case est occupée , veuillez en choisir une autre")
            else:
                print("Veuillez entrer des coordonnées valides entre 1 et " + str(longueur) + ".")
        except ValueError:
            print("Mettre un chiffre valide")


def tour_adversaire(grille, pion_adversaire, pion_joueur):
    print("Tour de l'adversaire")
    taille = len(grille)

    # 1. Vérifier s'il existe une case pour gagner
    for i in range(taille):
        for j in range(taille):
            if grille[i][j] == " ":
                grille[i][j] = pion_adversaire
                if victoire(grille, pion_adversaire):
                    return
                grille[i][j] = " "
    # 2. Vérifier s'il existe une case à bloquer
    for i in range(taille):
        for j in range(taille):
            if grille[i][j] == " ":
                grille[i][j] = pion_joueur
                if victoire(grille, pion_joueur):
                    grille[i][j] = pion_adversaire
                    return
                grille[i][j] = " "

    # 3. Jouer de manière aléatoire si aucune stratégie spécifique n'est applicable
    while True:
        ligne = random.randint(0, taille - 1)
        colonne = random.randint(0, taille - 1)
        if placer_pion(grille, ligne, colonne, "O"):
            break


#######################################################################################################################

# Fonction principale qui initialise le jeu, et va appeler les fonctions nécessaires au déroulement de la partie
def morpion():
    taille = int(input("Entrez la taille de la grille (minimum 3) : "))
    while taille < 3:
        print("La taille minimum est de 3.")
        taille = int(input("Entrez la taille de la grille : "))
    rejouer = True
    while rejouer:
        grille = creer_grille(taille)
        tour = 0
        afficher_grille(grille)
        while True:
            tour += 1
            print("Tour numéro : ", tour)
            tour_joueur(grille)
            if victoire(grille, "X"):
                afficher_grille(grille)
                print('Match gagné!')
                break
            if tour == taille * taille:
                afficher_grille(grille)
                print('Match nul !')
                break
            tour_adversaire(grille, "O", "X")
            afficher_grille(grille)
            if victoire(grille, "O"):
                afficher_grille(grille)
                print('Match perdu!')
                break
        rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower() == 'o'


# Débute le jeu dès le lancement du script

morpion()

