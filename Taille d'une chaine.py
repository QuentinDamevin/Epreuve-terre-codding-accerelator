#Creez un programme qui affiche le nombre de caracteres d'une chaîne de caractères passée en argument.

import sys

arguments = sys.argv

if len(arguments) != 2 : 
    print("erreur")
    exit()


arguments_1 = arguments[1]
if arguments_1.isnumeric():
    print("erreur")
    exit()
else:
    print(len(arguments_1))