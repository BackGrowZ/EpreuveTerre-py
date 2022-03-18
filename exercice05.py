# Afficher le résultat et le reste d'une division passée en argument

import sys

try:
    dividende = int(sys.argv[1])
    diviseur = int(sys.argv[2])
except:
    print("Veuillez rentrer 2 nombres entiers")
else:
    if diviseur == 0:
        print("On ne peut pas diviser par 0")
    elif 0 <= dividende < diviseur :
        print("Veuilez rentrer un premmier nombre plus grand que le deuxième")
    else:
        resultat = dividende // diviseur
        reste = dividende % diviseur
        print("Résultat : " + str(resultat))
        print("Reste: " + str(reste))

