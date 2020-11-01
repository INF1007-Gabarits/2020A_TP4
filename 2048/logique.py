# logique.py est importé par gui.py
# Ce fichier consiste en la logique du jeu 2048 

import random
import constantes as c

# TODO: 
# Initialisation du jeu
# 1. Dans une nouvelle matrice, ajouter deux fois un 2 ou un 4
def demarrer_jeu(): 
    ...
    return ...

#TODO:
# Retourner une nouvelle matrice 4x4 remplie de 0
def initialiser_nouvelle_matrice():
    ...
    return ...

# TODO:
# Ajout d'un 2 ou d'un 4 a la matrice du jeu avec des probabilités de: 90% 2 et 10% 4
# dans un emplacement vide aléatoire de la matrice (emplacement == 0)
def ajouter_nouveau_2_ou_4(grille):
    ...
    return ...
  
# TODO: 
# Retourner l'état du jeu
# 1. Victoire
#   a) Si un element de la matrice == 2048
# 2. Le jeu n'est pas fini
#   a) S'il y a au moins un element == 0
#   b) OU S'il n'y a aucune cellule vide, MAIS qu'il y a un (ou des) mouvements possibles
# 3. Défaite
#   a) Les cas restants
def get_etat_jeu_courant(grille):
    ...
    return ...
  
# NOTE: Les fonctions suivantes sont pour le mouvement gauche seulement 
  
# TODO: 
# Comprimer la matrice de jeu.
# À effectuer après toutes les étapes avant et après le fusionnement des éléments
#   a) Initialiser une nouvelle matrice remplie de 0 initialement.
#   b) Bouger tous les elements à son extrême gauche, lorsque possible
#       b.a) SEULEMENT possible lorsque l'élément à gauche == 0
#       b.b) PAS POSSIBLE si gauche != 0
#   c) Retourner la nouvelle matrice comprimée, avec un booléen indicant s'il y a au moins eu 1 changement
def comprimer(matrice):
    ...
    return ...
  
# TODO:
# Fusionner les éléments de la matrice après une compression
# 1) Si l'élément a la même valeur que le prochain élément dans la ligne
#    ET qu'ils sont non vide (!= 0)
#    ALORS doubler la valeur de l'élément courant ET vider l'élément suivant
# 2) Retourner la matrice fusionnée et un booléen indicant s'il y a eu un changement
def fusionner(matrice):
    ...
    return ...

# TODO: 
# Inverser la matrice
# 1) Dans une nouvelle matrice,
#    inverser la séquence dans chaque ligne de la matrice
# 2) Retourner la nouvelle matrice
def inverser(matrice):
    ...
    return ...
  
# TODO:
# Transposer la matrice
# 1) Dans une nouvelle matrice,
#    Échanger les lignes avec les colomnes
# 2) Retourner la nouvelle matrice
def transposer(matrice):
    ...
    return ...

# NOTE: Les fonctions suivantes servent à gérer un mouvement dans la matrice.

#TODO: 
# Bouger la matrice à gauche
# 1) Dans une nouvelle matrice
#   a) Comprimer la matrice
#   b) Fusionner la matrice
#   c) Recomprimer la matrice
# 2) Retourner la nouvelle matrice, ainsi qu'un booléen indicant s'il y a eu un changement
def faire_translation_gauche(matrice):
    ...
    return ...
  
#TODO: 
# Bouger la matrice à droite
# 1) Dans une nouvelle matrice
#   a) Inverser la matrice pour simuler un mouvement à gauche
#   b) Bouger la matrice à gauche
#   c) Re-inverser la matrice
# 2) Retourner la nouvelle matrice, ainsi qu'un booléen indicant s'il y a eu un changement
def faire_translation_droite(matrice):
    ...
    return ...
  
#TODO: 
# Bouger la matrice en haut
# 1) Dans une nouvelle matrice
#   a) Transposer la matrice pour simuler un mouvement à gauche
#   b) Bouger la matrice à gauche
#   c) Re-transposer la matrice
# 2) Retourner la nouvelle matrice, ainsi qu'un booléen indicant s'il y a eu un changement
def faire_translation_haut(matrice):
    ...
    return ...
  
#TODO: 
# Bouger la matrice en bas
# 1) Dans une nouvelle matrice
#   a) Transposer la matrice pour simuler un mouvement à droite
#   b) Bouger la matrice à droite
#   c) Re-transposer la matrice
# 2) Retourner la nouvelle matrice, ainsi qu'un booléen indicant s'il y a eu un changement
def faire_translation_bas(matrice):
    ...
    return ...