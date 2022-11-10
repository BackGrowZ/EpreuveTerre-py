# Affiche le résultat d'une puissance
# L'exposant ne doit pas être négatif

import sys

def puissance(nombre, exposant):
    return nombre ** exposant

try:
    nb1 = int(sys.argv[1])
    nb2 = int(sys.argv[2])
except IndexError:
    print("Veuillez rentrer des arguments")
except ValueError:
    print("Veuillez rentrer des nombres corrects")
else:
    if nb2 < 0:
        print("L'exposant ne peut pas être négatif")
    elif nb2 == 0:
        print("1")
    else:
        print(str(puissance(nb1,nb2)))