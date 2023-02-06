#Creez un programme qui prend en parametre trois entiers et affiche la valeur du milieu
#Trouver la suisse (lol)

import sys


arguments = sys.argv

try:
    int(arguments[1])
    
except:
    print("Vous devez rentrer des nombres")

if len(arguments) != 4:
    print("Vous devez saisir 3 nombre séparé")
    exit()


a = int(arguments[1])
b = int(arguments[2])
c = int(arguments[3])



list_nombres = a,b,c

liste_trie = sorted(list_nombres)

print(liste_trie[1])
