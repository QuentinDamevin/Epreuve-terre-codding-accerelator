import sys

arguments = sys.argv
arguments_1 = arguments[1]


if len(arguments) != 2:
    print("Erreur 1 argument requis")
    exit()

if "AM" in arguments_1 and arguments_1[0:2] == "12":
    h = ("00" + arguments_1[2:5])
    print(h)

if "AM" in arguments_1:
    h = arguments_1[0:5]
    print(h)


if("PM" in arguments_1 and arguments_1[:2] == "12"):
    op = arguments_1[:-2]
    print(op)


elif "PM" in arguments_1:
     h =  str(int(arguments_1[0:2]) + 12) + arguments_1[2:5]
     print(h)
    

else:
    print("Veuillez entrer HH:MM:PM OU AM")




