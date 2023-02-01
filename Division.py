#Creez un programme qui affiche le resultat et le reste d'une division entre deux nombres.
import sys

arguments_division  = sys.argv
try:
    
    resultats_division = int(arguments_division[1]) // int(arguments_division[2])
    if resultats_division <= 0:
        exit()
    reste_resultats_division = int(arguments_division[1]) % int(arguments_division[2])
    print(f"Le resultats est : {resultats_division}")
    print(f"Le reste de la division est :  {reste_resultats_division}")

except:
    print("Erreur")
    exit()


