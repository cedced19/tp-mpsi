#!/usr/bin/python3
import random
print("Jeu du nombre secret ")
n= random.randint(0,99)
print("J'ai choisi un nombre secret entre 0 et 99")

e=1
p = int(input("Devines "));
while(p != n):
	e+=1
	print("Incorrect")
	if (p > n):
		print("C'est un nombre plus petit")
	else:
		print("C'est un nombre plus grand");
	p = int(input("Devines "));
print("Correct, réussi en {} essai(s)".format(e))