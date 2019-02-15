from fractions import Fraction

def check (r): # Vérification 
    s = 0
    for i in range(len(r)):
        s+=Fraction(1,r[i])
    return(s==1)

def rec (A, N):
    # On constate que pour trouver le x_p suivant il faut majoré par (N-len(A))/(1-1/x_0-1/x_1-...-1/x_p-1)
    # où len(A) est le nombre d'éléments trouvés
    # et N le nombre d'éléments à trouver
    L=[]
    m=1
    for val in A:
        m=m-1/val
    if (round(m,10)<=0): # Si le flottant est trop proche de zero on le supprime, il doit y avoir un moyen de mieux faire, et de réduire les cas
        return L
    M=round((N-len(A))/m)
    c=M
    if (len(A)!=N-1):
        while (c<=M and c>=A[-1]):
            L.append([*A, c])
            c-=1
    else: # Si il n'y a plus qu'un nombre à trouver alors cela doit forcément être solution
        while (c<=M and c>=A[-1]):
            if (check([*A, c])):
                #print([*A, c])
                L.append([*A, c])
                return L
            c-=1
    return L

def solve (N):
    L=[[N]*N] # On ajoute directement la solution évidente
    x = []
    for i in range(2, N):
        x.append([i])
    count=1
    while (count<N): # On construit la suite de proche en proche
        Lt=[]
        for k in range (len(x)):
            for val in rec(x[k], N):
                if (len(val) != 0):
                    Lt.append(val)
        x=Lt
        count+=1
    for i in x:
        L.append(i)
    return L, len(L)

# Tests
print(solve(3))
print(solve(4))
print(solve(5))
#print(solve(6))