
def chiffre (c): 
    n = str(c)
    arr = []
    for i in range(0,len(n)):
        arr.append(int(n[i]))
    return arr

print(chiffre(1234))

def liste (arr):
    c=0
    n=len(arr)
    for i in range(n):
        c += arr[i]*10**(n-1-i)
    return c

print(liste([1, 2, 3, 4]))

def decroissant (c):
    arr = chiffre(c)
    def echange (i,j):
        u = arr[i]
        arr[i]=arr[j]
        arr[j]=u
    # tri selection
    n = len(arr)
    ind_max = 0
    for i in range(n):
        ind_max = i
        for j in range(i+1,n):
            if (arr[j] > arr[ind_max]):
                ind_max = j
        echange(i, ind_max)
    return liste(arr)
                
print(decroissant(8459))

def croissant (c):
    arr = chiffre(c)
    def echange (i,j):
        u = arr[i]
        arr[i]=arr[j]
        arr[j]=u
    # tri selection
    n = len(arr)
    ind_min = 0
    for i in range(n):
        ind_min = i
        for j in range(i+1,n):
            if (arr[j] < arr[ind_min]):
                ind_min = j
        echange(i, ind_min)
    return liste(arr)

print(croissant(8459))

def Kaprekar (n):
    return decroissant(n)-croissant(n)

print(Kaprekar(1826))

def test_val_kaprekar (init, final, val):
    arr = []
    for i in range(init,final+1):
        if (Kaprekar(i) == val):
            arr.append(i)
    return arr

print(test_val_kaprekar(1000,9999, 0))
print(test_val_kaprekar(1000,9999, 999))

def test_id_kaprekar (init, final):
    arr = []
    for i in range(init,final+1):
        if (Kaprekar(i) == i):
            arr.append(i)
    return arr

print(test_id_kaprekar(1000,9999)) # Seul 6174 convient

def Kaprekar_it (n,i):
    c=n
    for i in range(i):
        c=Kaprekar(c)
    return c

print(Kaprekar_it(1826,2))

def chaine (n):
    c=n
    arr=[n]
    while (c != 6174 and c != 0): 
        c=Kaprekar(c)
        arr.append(c)
    return arr

print(chaine(1826))

def min_it (init, final, j):
    arr = []
    for i in range(init,final+1):
        if (len(chaine(i)) == j):
            arr.append(i)
    return arr

print(min_it(1000,9999, 8))
print(chaine(9006))