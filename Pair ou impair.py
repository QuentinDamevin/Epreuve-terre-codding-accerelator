#Pair ou impair
# Creez un programme qui permet de déterminer si l'argument donné est un entier pair ou impair.

import sys

argument_nombre = sys.argv

try:
    if int(argument_nombre[1]) % 2 == 0: 
        print("Pair")
    else:
        print("Impair")

except:
    print("Tu ne me la mettras pas a l'envers")
    exit()



