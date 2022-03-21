# Convertit l'heure du format 24h au format 12h

import sys


def convertir(h, m):
    resultat = ""
    if int(h) < 0 or int(h) > 24 or len(str(h)) > 2:
        print("Veuillez rentrer une heure correcte")
        return
    elif int(m) < 0 or int(m) > 60 or not len(str(m)) == 2:
        print("Veuillez rentrer une minute correcte")
        return        
    if int(h) <= 12:
        resultat = str(h) + ":" + str(minute) + "AM"
    else:
        h = int(h) - 12
        resultat = str(h) + ":" + str(minute) + "PM"
    return resultat

try:
    heure_24 = sys.argv[1].split(":")
    heure = heure_24[0]
    minute = heure_24[1]
except IndexError:
        print("Veuillez passer un argument")
else:
    if not convertir(heure, minute) == None:
        print(convertir(heure, minute))