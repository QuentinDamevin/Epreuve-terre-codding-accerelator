import sys 

arguments = sys.argv

if len(arguments) != 2:
    print("erreur")
    exit()


arguments_1 = arguments[1]

if arguments_1.isnumeric():
    print("Erreur")
    exit()

else:
    print(arguments_1[::-1])