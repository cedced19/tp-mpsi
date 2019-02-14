from fractions import Fraction

def rec (A, N):
    # On constate que pour trouver le x_p suivant il faut majoré par (N-len(A))/(1-1/x_0-1/x_1-...-1/x_p-1)
    # où len(A) est le nombre d'éléments trouvés
    # et N le nombre d'éléments à trouver
    L=[]
    m=1
    for val in A:
        m=m-1/val
    if (round(m,15)==0): # Si le flottant est trop proche de zero on le supprime, il doit y avoir un moyen de mieux faire, et de réduire les cas
        return L
    M=round((N-len(A))/m)
    c=M
    while (c<=M and c>=A[-1]):
        L.append([*A, c])
        c-=1
    return L

def rec2 (x, N): # Construction des listes de proche en proche
    L=[[x]]
    count=1
    while (count<N):
        Lt=[]
        for k in range (len(L)):
            for val in rec(L[k], N):
                Lt.append(val)
        L=Lt
        count+=1
    return L


def check (r): # Vérification 
    s = 0
    for i in range(len(r)):
        s+=Fraction(1,r[i])
    return(s==1)

def solve (N):
    L=[[N]*N] # On ajoute directement la solution évidente
    for i in range(2, N):
        r = rec2(i, N)
        for i in r:
            if(check(i)): # Vérification
                L.append(i)
    return L, len(L)

# Tests
print(solve(3))
print(solve(4))
print(solve(5))