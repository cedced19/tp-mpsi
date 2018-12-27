#!/usr/bin/python3

L=list([i for i in range(1,100)])

somme=0
produit=1

for val in L:
	somme += val
	produit *= val
moyenne=somme/len(L)
print("La somme recherchée est {}\n".format(somme))
print("Le produit recherchée est {}\n".format(produit))
print("La moyenne recherchée est {}\n".format(moyenne))