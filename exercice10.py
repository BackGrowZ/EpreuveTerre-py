# Affiche si un nombre et premier
# 0 et 1 ne sont pas des nombres premiers

import sys

def est_premier(nb):
    
    for i in range(2, nb):
        if nb % i == 0:
            return False
    return True
          
try:
    nb_user = int(sys.argv[1])
except ValueError:
    print("Veuillez rentrer un entier positif")
except IndexError:
    print("Veuillez rentrer un argument")
else:
    if nb_user < 0:
        print("Veuillez rentrer un nombre positif")
    elif nb_user == 0 or nb_user == 1 or not est_premier(nb_user):
        print(str(nb_user) + " n'est pas un nombre premier")
    else:
        print(str(nb_user) + " est un nombre premier")
