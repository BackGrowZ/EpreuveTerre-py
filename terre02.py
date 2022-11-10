# Affiche les arguments qu'il recoit, peu importe leur nombre
import sys

if len(sys.argv) ==  1:
    print("Veuillez rentrer au moins un argument")
else:
    for i in range(1, len(sys.argv)):
        print(sys.argv[i])