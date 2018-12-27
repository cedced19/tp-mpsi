#!/usr/bin/python3

n=int(input("Indice du terme à calculer\n"))

u, v = 0, 1
for i in range(0,n):
	u, v=v, u+v
print("le nombre de Fibonacci d'indice {} est  {}".format(n,u))
