# Affiche la valeur du milieu entre 3 entiers donnés

import sys

def trouver_la_suisse(a, b, c):
    
    if a == b or a == c or b == c:
        print("Veuillez rentrer 3 nombres différents")
        return
    
    if a < b:
        if a < c:
            if b < c:
                return b
            else:
                return c
        else:
            return a
    else:
        if a < c:
            return a
        else:
            if b < c:
                return c
            else:
                return b
    return

try:
    nb1 = int(sys.argv[1])
    nb2 = int(sys.argv[2])
    nb3 = int(sys.argv[3])
except ValueError:
    print("Veuillez rentrer 3 nombres corrects")
except IndexError:
    print("Veuillez passer 3 nombres en argument")
else:
    if not trouver_la_suisse(nb1, nb2, nb3) == None:
        print(str(trouver_la_suisse(nb1, nb2, nb3)))