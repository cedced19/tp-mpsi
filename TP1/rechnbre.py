#!/usr/bin/python3

L=[4,3,8,1,7]


def rechercher(n):
	for val in L:
		if (val==n):
			return True
	return False
	
print(rechercher(5)) # on recherche 5 doit renvoyer False
print(rechercher(7)) # on recherche 7 doit renvoyer True