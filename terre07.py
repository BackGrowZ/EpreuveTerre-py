# Afficher la taille d'une chaîne de caractère passée en argument

import sys

def compter_chaine(chaine):
    count = 0
    if not len(sys.argv) == 2:
        print("Veuillez rentrer une unique chaîne de caractère")
        return
    elif txt_user.isdigit():
        print("Veuillez rentrer de chaîne correcte")
        return
    else:
        for i in chaine:
            count = count + 1
        return str(count)
    

try:
    txt_user = sys.argv[1]
except IndexError:
    print("Veuillez passer un argument")
else:
    if not compter_chaine(txt_user) == None:
        print(compter_chaine(txt_user))