# Convertit l'heure du format 24h au format 12h

import sys


def convertir(h, m):
    resultat = ""
    if h <= 0 or h > 24 or len(str(h)) > 2:
        print("Veuillez rentrer une valeur correcte pour l'heure")
        return
    elif m <= 0 or m > 60 or not len(str(m)) == 2:
        print("Veuillez rentrer une valeur correcte pour la minute")
        return        
    
    if h <= 12:
        resultat = str(h) + ":" + str(m) + "AM"
    else:
        h = h - 12
        resultat = str(h) + ":" + str(m) + "PM"
    return resultat

try:
    heure_24 = sys.argv[1].split(":")
    heure = int(heure_24[0])
    minute = int(heure_24[1])
except IndexError:
        print("Veuillez passer un argument")
except ValueError:
        print("Veuillez rentrer une heure correcte")
else:
    if not convertir(heure, minute) == None:
        print(convertir(heure, minute))