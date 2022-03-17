# Affiche les arguments qu'il recoit, peu importe leur nombre
import sys

argument_list = sys.argv

for i in range(1, len(argument_list)):
    print(argument_list[i])