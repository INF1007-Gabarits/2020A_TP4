# Définissez et implémentez ici la liste des fonctions de tests responsables des tests de chacune des fonctions de
# logique.py
def tester_inverser_matrice_identite():
    matrice = [[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]
    ...
    return ...


def ecrire_resultat_test(test, resultat):
    reussite_ou_echec = ("Échec", "Réussite")[resultat]
    print(test + "..." + reussite_ou_echec)


if __name__ == '__main__':
    ecrire_resultat_test(tester_inverser_matrice_identite.__name__, tester_inverser_matrice_identite())
