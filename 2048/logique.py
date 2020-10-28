# logique.py est importé par gui.py
# Ce fichier consiste en la logique du jeu 2048 

import random
import constantes as c

# TODO: 
# Initialisation du jeu
# 1. Dans une nouvelle matrice, ajouter deux fois un 2 ou un 4
def demarrer_jeu(): 
    mat = initialiser_nouvelle_matrice()
  
    for _ in range(2):
        ajouter_nouveau_2_ou_4(mat)

    return mat 

#TODO:
# Retourner une nouvelle matrice 4x4 remplie de 0
def initialiser_nouvelle_matrice():
    mat =[] 
    for _ in range(4): 
        mat.append([0] * 4) 
    
    return mat

# TODO:
# Ajout d'un 2 ou d'un 4 a la matrice du jeu avec des probabilités de: 90% 2 et 10% 4
# dans un emplacement vide aléatoire de la matrice (emplacement == 0)
def ajouter_nouveau_2_ou_4(mat): 
  
    r = random.randint(0, 3) 
    c = random.randint(0, 3) 
  
    while(mat[r][c] != 0): 
        r = random.randint(0, 3) 
        c = random.randint(0, 3) 
    
    if random.randint(0, 10) == 0:
        mat[r][c] = 4
    else:
        mat[r][c] = 2

    return mat
  
# TODO: 
# Retourner l'état du jeu
# 1. Victoire
#   a) Si un element de la matrice == 2048
# 2. Le jeu n'est pas fini
#   a) S'il y a au moins un element == 0
#   b) OU S'il n'y a aucune cellule vide, MAIS qu'il y a un (ou des) mouvements possibles
# 3. Défaite
#   a) Les cas restants
def get_etat_jeu_courant(mat): 
  
    for i in range(4): 
        for j in range(4): 
            if(mat[i][j]== int(c.TITRE)): 
                return c.ETAT_VICTOIRE
  
    for i in range(4): 
        for j in range(4): 
            if(mat[i][j]== 0): 
                return c.ETAT_PARTIE_EN_COURS
  
    for i in range(3): 
        for j in range(3): 
            if(mat[i][j]== mat[i + 1][j] or mat[i][j]== mat[i][j + 1]): 
                return c.ETAT_PARTIE_EN_COURS
  
    for i in range(3): 
        if(mat[3][i]== mat[3][i + 1]) or (mat[i][3]== mat[i + 1][3]): 
            return c.ETAT_PARTIE_EN_COURS
  
    return c.ETAT_DEFAITE
  
# NOTE: Les fonctions suivantes sont pour le mouvement gauche seulement 
  
# TODO: 
# Comprimer la matrice de jeu.
# À effectuer après tous les étapes avant et après le fusionnement des éléments
#   a) Initialiser une nouvelle matrice remplie de 0 initialement.
#   b) Bouger tous les elements à son extrême gauche, lorsque possible
#       b.a) SEULEMENT possible lorsque l'élément à gauche == 0
#       b.b) PAS POSSIBLE si gauche != 0
#   c) Retourner la nouvelle matrice comprimée, avec un booléen indicant s'il y a au moins eu 1 changement
def comprimer(mat): 
  
    a_au_moins_un_changement = False  
    nouvelle_matrice = initialiser_nouvelle_matrice()

    for i in range(4): 
        derniere_position = 0
  
        for j in range(4): 
            if(mat[i][j] != 0): 
                nouvelle_matrice[i][derniere_position] = mat[i][j] 
                  
                if(j != derniere_position): 
                    a_au_moins_un_changement = True
                
                derniere_position += 1
  
    return nouvelle_matrice, a_au_moins_un_changement 
  
# TODO:
# Fusionner les éléments de la matrice après une compression
# 1) Si l'élément a la même valeur que le prochain élément dans la ligne
#    ET qu'ils sont non vide (!= 0)
#    ALORS doubler la valeur de l'élément courant ET vider l'élément suivant
# 2) Retourner la matrice fusionnée et un booléen indicant s'il y a eu un changement
def fusionner(mat): 
    a_au_moins_un_changement = False
      
    for i in range(4): 
        for j in range(3): 
            if(mat[i][j] == mat[i][j + 1] and mat[i][j] != 0): 
  
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
  
                a_au_moins_un_changement = True
  
    return mat, a_au_moins_un_changement 

# TODO: 
# Inverser la matrice
# 1) Dans une nouvelle matrice,
#    inverser la séquence dans chaque ligne de la matrice
# 2) Retourner la nouvelle matrice
def inverser(mat): 
    nouvelle_matrice =[] 
    for i in range(4): 
        nouvelle_matrice.append([]) 
        for j in range(4): 
            nouvelle_matrice[i].append(mat[i][3 - j]) 
    return nouvelle_matrice 
  
# TODO:
# Transposer la matrice
# 1) Dans une nouvelle matrice,
#    Échanger les lignes avec les colomnes
# 2) Retourner la nouvelle matrice
def transposer(mat): 
    nouvelle_matrice = [] 
    for i in range(4): 
        nouvelle_matrice.append([]) 
        for j in range(4): 
            nouvelle_matrice[i].append(mat[j][i]) 
    return nouvelle_matrice 
  

# NOTE: Les fonctions suivantes servent à gérer un mouvement dans la matrice.

#TODO: 
# Bouger la matrice à gauche
# 1) Dans une nouvelle matrice
#   a) Comprimer la matrice
#   b) Fusionner la matrice
#   c) Recomprimer la matrice
# 2) Retourner la nouvelle matrice, ainsi qu'un booléen indicant s'il y a eu un changement
def bouger_matrice_a_gauche(matrice): 
    nouvelle_matrice, changement1 = comprimer(matrice) 

    nouvelle_matrice, changement2 = fusionner(nouvelle_matrice) 
      
    a_au_moins_un_changement = changement1 or changement2 
   
    nouvelle_matrice, _ = comprimer(nouvelle_matrice) 
  
    return nouvelle_matrice, a_au_moins_un_changement 
  
#TODO: 
# Bouger la matrice à droite
# 1) Dans une nouvelle matrice
#   a) Inverser la matrice pour simuler un mouvement à gauche
#   b) Bouger la matrice à gauche
#   c) Re-inverser la matrice
# 2) Retourner la nouvelle matrice, ainsi qu'un booléen indicant s'il y a eu un changement
def bouger_matrice_a_droite(matrice): 
    nouvelle_matrice = inverser(matrice) 
  
    nouvelle_matrice, a_au_moins_un_changement = bouger_matrice_a_gauche(nouvelle_matrice) 
  
    nouvelle_matrice = inverser(nouvelle_matrice)

    return nouvelle_matrice, a_au_moins_un_changement 
  
#TODO: 
# Bouger la matrice en haut
# 1) Dans une nouvelle matrice
#   a) Transposer la matrice pour simuler un mouvement à gauche
#   b) Bouger la matrice à gauche
#   c) Re-transposer la matrice
# 2) Retourner la nouvelle matrice, ainsi qu'un booléen indicant s'il y a eu un changement
def bouger_matrice_en_haut(matrice): 
    nouvelle_matrice = transposer(matrice) 
  
    nouvelle_matrice, a_au_moins_un_changement = bouger_matrice_a_gauche(nouvelle_matrice) 
   
    nouvelle_matrice = transposer(nouvelle_matrice)

    return nouvelle_matrice, a_au_moins_un_changement 
  
#TODO: 
# Bouger la matrice en bas
# 1) Dans une nouvelle matrice
#   a) Transposer la matrice pour simuler un mouvement à droite
#   b) Bouger la matrice à droite
#   c) Re-transposer la matrice
# 2) Retourner la nouvelle matrice, ainsi qu'un booléen indicant s'il y a eu un changement
def bouger_la_matrice_en_bas(matrice): 
    nouvelle_matrice = transposer(matrice) 
  
    nouvelle_matrice, a_au_moins_un_changement = bouger_matrice_a_droite(nouvelle_matrice) 
  
    nouvelle_matrice = transposer(nouvelle_matrice) 

    return nouvelle_matrice, a_au_moins_un_changement 