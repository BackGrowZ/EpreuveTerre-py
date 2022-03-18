# Affiche l'inverse d'une chaîne de caractères passée en argument

import sys


def inverser_texte(chaine):
    chaine_retournee = []
    for i in chaine:
        chaine_retournee.insert(0,i)
    for j in chaine_retournee:
        print(j, end="")
    print()


try:
    txt_user = sys.argv[1]
except IndexError:
    print("Veuillez passer un argument")
else:
    if not len(sys.argv) == 2:
        print("Veuillez rentrer une unique chaîne de caractère")
    elif txt_user.isdigit():
        print("Veuillez rentrer de chaîne correcte")
    else:
        inverser_texte(txt_user)
        