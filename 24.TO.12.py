#Creez un programme qui transforme une heure affiché en format 24 h en une heure affiché en format 12.
#Attention : midi et minuit
import sys

arguments = sys.argv

try:
    arguments_1 = arguments[1]

except:
    print("Veuillez entrer HH:MM")

if len(arguments) != 2:
    print("Erreur 1 argument requis")
    exit()


if arguments_1  <= "00:59":
    h =  str(int(arguments_1[0:2]) + 12) + arguments_1[2:5] + "PM"
    print(h)
    
elif arguments_1 <= "12:59":
    h = arguments_1 + "AM"
    print(h)


elif arguments_1 >= "13:00":
    h =  str(int(arguments_1[0:2]) - 12) + arguments_1[2:5] + "PM"
    print(h)
    

else:
    print("Veuillez entrer HH:MM")



