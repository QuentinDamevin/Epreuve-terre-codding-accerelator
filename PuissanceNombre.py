#Creez un programme qui affiche le résultat d'une puissance.

import sys

arguments = sys.argv

try:
    arguments_1 = int(arguments[1])
    arguments_2 = int(arguments[2])

except:
    print("erreur")
    exit()

if arguments_1 ** arguments_2 <= 0:
    print("Erreur le nombre est négatif")
    exit()
if len(arguments) !=3:
    print("Erreur veuillez rentrer deux arguments")

else:
    print(arguments_1**arguments_2)



