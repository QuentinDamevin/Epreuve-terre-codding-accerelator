#Créez un programme qui détermine si une liste d’entiers est triée ou pas.
import sys

arguments = sys.argv

try:
    int(arguments[1])
    
except:
    print("Vous devez rentrer des nombres")
    exit()

if len(arguments) < 4:
    print("Vous devez saisir minium 3 nombre séparé")
    exit()

arguments_int =[int(x) for x in arguments[1:]]
n = sorted(arguments_int)

if arguments_int == n:
    print("Liste triés")
else:
    print("Liste non triés")
