# Afficher la racine carrée d'un entier positif

import sys

def racine_carree(nb):
    resultat = nb ** (1/2)
    if resultat.is_integer():
        return int(resultat)
    else:
        return resultat

try:
    nb_user = int(sys.argv[1])
except ValueError:
    print("Veuillez rentrer un entier positif")
except IndexError:
    print("Veuillez rentrer un argument")
else:
    if nb_user < 0:
        print("Veuillez rentrer un nombre positif")
    else:
        print(str(racine_carree(nb_user)))
