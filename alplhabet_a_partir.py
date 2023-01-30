#creez un programme qui affiche l'alphabet en minuscule a partir de la lettre donée en argument suivi d'un retour a la ligne
import string
import sys
arguments = sys.argv
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z"]
alphabet_string = str(alphabet)
index_lettre_depart = (alphabet_string.index(arguments[1]))

for i in alphabet[index_lettre_depart:-1]:
    print(i ,end="")

print()





#print(str(alphabet)[index_lettre_depart:-1])



