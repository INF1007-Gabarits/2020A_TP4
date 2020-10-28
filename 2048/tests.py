def tester_inverser():
    return True

def ecrire_resultat_test(test, resultat):
    reussite_ou_echec = ("Échec", "Réussite")[resultat]
    print(test + "..." + reussite_ou_echec)


if __name__ == '__main__':
    ecrire_resultat_test(tester_inverser.__name__, tester_inverser())

