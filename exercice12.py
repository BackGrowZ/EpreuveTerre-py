# Convertit l'heure du format 12h au format 24h

import sys

def convertir(h, m, am_pm):
    resultat = ""
    if len(str(h)) > 2 or int(h) > 24 or int(h) < 0 :
        print("Veuillez rentrer une heure correcte")
        return
    elif not len(str(m)) == 2 or int(m) > 60 or int(m) < 0:
        print("Veuillez rentrer une minute correcte")
        return        
    

    if am_pm:
        if int(h) == 12 and int(m) == 00:
            resultat = "00:00"
        else:
            resultat = str(h) + ":" + str(m)
    else:
        if int(h) == 12 and int(m) == 00:
            resultat = "12:00"
        else:
            h = int(h) + 12
            if h == 24:
                resultat = "00:" + str(m)
            else:
                resultat = str(h) + ":" + str(m)
    return resultat

try:
    heure_24 = sys.argv[1].split(":")
    is_matin = str(heure_24[1]).endswith("AM")
    heure = heure_24[0]
    minute = heure_24[1].replace("AM", "").replace("PM", "")
except IndexError:
        print("Veuillez passer un argument correct")
else:
    if not convertir(heure, minute, is_matin) == None:
        print(convertir(heure, minute, is_matin))   