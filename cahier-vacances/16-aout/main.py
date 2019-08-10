from random import randint


def one_step_with_replace ():
    # tirage avec remise
    X = 0
    for i in range(5): 
        v = randint(1, 8)
        if (v > 8): # au dessus de 8 on obtient une boule blanche 
            X+=1   # on compte le nombre de boule blanche
    Y=X*2+(5-X)*(-3)
    return (X, Y)


def one_step_without_replace ():
    # tirage sans remise
    X = 0
    initial=1
    final=10
    for i in range(5): 
        v = randint(initial, final) # au dessus de 8 on obtient une boule blanche 
        if (v > 8): 
            X+=1
            final=final-1 # on enlève la possiblité d'obtenir une boule blanche
        else:
            initial=initial+1 # on enlève la possiblité d'obtenir une boule noire
    Y=X*2+(5-X)*(-3)
    return (X, Y)

def esperance (func, n):
    arrX = [0]*6
    arrY = {}
    for i in range(n+1):
        (X, Y) = func()
        arrX[X]+=1
        arrY[Y]=1+arrY.get(Y, 0)
    esperanceX = 0
    for i in range(6):
        esperanceX+= arrX[i]*i*(1/n)
    esperanceY = 0
    for i in arrY.keys():
        esperanceY+= arrY[i]*i*(1/n)
    return (esperanceX, esperanceY)
    

print(esperance(one_step_with_replace, 1000000))
print(esperance(one_step_without_replace, 1000000))