# Creez un programme qui affiche la racine carrée d'un entier positif.

import sys
import math
arguments = sys.argv

try:
    int_arguments = int(arguments[1])

except:
    print("Vous devez rentrer un nombre")
    exit()

if len(arguments) != 2:
    print("Erreur")
    exit()

else:
    print(math.sqrt(int(arguments[1])))