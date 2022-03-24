# Détermine si une liste d'entier est triée

import sys

def est_triee(liste):
    for i in range(0, len(liste) - 1):
        if liste[i] > liste[i + 1]:
            return False
        return True
    
try: 
    number_list = []
    for i in range(1, len(sys.argv)):
        number_list.append(int(sys.argv[i]))
except IndexError:
    print("Veuillez rentrer un argument")
except ValueError:
    print("Veuillez rentrer une liste d'entiers")
else:
    if len(number_list) == 0:
        print("Veuillez rentrer un argument")
    elif est_triee(number_list):
        print("Triée")
    else:
        print("Pas triée")

