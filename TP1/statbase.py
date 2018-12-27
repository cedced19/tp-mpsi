#!/usr/bin/python3

L=[4,3,8,1,7] # [50,1,-1,3,8,70,5,4,9,17]

somme = 0;


maxi = L[0]
mini = L[0]
for i in range(0, len(L)):
	somme += L[i]
	if (L[i]>maxi):
		maxi = L[i]
	if (L[i]<mini):
		mini = L[i]

moyenne=somme/len(L)

variance = 0
for i in range(0, len(L)):
	variance += (L[i] - moyenne)**2
	
variance= variance/len(L)

print("La valeur maximum est {}\n".format(maxi))
print("La valeur minimum est {}\n".format(mini))
print("La somme est {}\n".format(somme))
print("La moyenne est {}\n".format(moyenne))
print("La variance est {}\n".format(variance))