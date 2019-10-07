#Exercice 1
print "Entrer un nombre entier"
Nombre = input()
for i in range (0,Nombre+1):
    print i
    if i%2 == 0:
        print "Pair"
    else:
        print "Impair" 

#Exercice 2
import random
r = random.randint(1,10)
Nombre = 0
while (Nombre != r):
    print "Entrez un nombre"
    Nombre = input()
    if Nombre < r:
        print "C'est plus !"
    elif Nombre > r:
        print "C'est moins !"
    else:
        print "reussi !"
        



