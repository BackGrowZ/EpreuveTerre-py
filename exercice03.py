# Afficher l'alphabet à partir d'une lettre donnée
# Condition : utiliser une boucle

import sys

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

try:
    arg_user = str(sys.argv[1])
    arg_pos = alphabet.index(arg_user)
except IndexError:
    print("Veuillez rentrer une lettre en minuscule")
except ValueError:
    print("Veuillez rentrer une lettre en minuscule")
else:    
    for i in range(arg_pos, len(alphabet)):
        print(alphabet[i], end="")
    print()