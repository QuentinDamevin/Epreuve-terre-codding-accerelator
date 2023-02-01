#Creez un programme qui affiche si un nombre est premier ou pas.
#ATTENTION : 0 ET 1 ne sont pas des nombres premiers. Gerez les erreurs d'arguments

import sys

arguments = sys.argv
try:
    int_arguments_1 = int(arguments[1])

except:
    print("Vous devez rentrer un nombre")
    exit()

if len(arguments) != 2:
    print("Erreur un argument maximum est admis")
    exit()

if int(arguments[1]) < 2:
    print(f" Non {arguments[1]} n'est pas un nombre entier")
    exit()

score = 0

for i in range(1,10):
    calcule = int(arguments[1]) % int(i)
    if calcule != 0:
        continue
    if calcule == 0:
        score +=1
    
if score == 2:
    print(f"Oui, {arguments[1]} est un nombre premier")
else:
    print(f"Non, {arguments[1]} n'est pas nombre premier")



      

