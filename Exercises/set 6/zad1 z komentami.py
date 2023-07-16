#program sprawdza dla każdej liczby czy jest ona wspólnoczynnikowa z jej sąsiadami
def czywspolno(a,b): #funkcja sprawdzająca czy dwie liczby są wspólno-czynnikowe
    wspolne = 0
    i=2
    while(a>1 or b>1):
        if(a%i==0 and b%i==0):
            wspolne+=1
            if(wspolne>1):
                return False
        while(a%i==0):
            a=a//i
        while(b%i==0):
            b=b//i
        i+=1
    if(wspolne==1):
        return True
    else:
        return False

def four(T):
    wynik = 0 #ilość liczb sąsiadujących z 4 liczbami wspólnoczynnikowymi
    vectors = [(-1,0),(0,-1),(0,1),(1,0)]
    n = len(T)
    for i in range(n):
        for j in range(n):
            sasiedzi = 0
            for vec in vectors:
                if(i+vec[0]>=0 and i+vec[0]<n and j+vec[1]>=0 and j+vec[1]<n):
                    if(czywspolno(T[i][j],T[i+vec[0]][j+vec[1]])):
                        sasiedzi+=1
            if(sasiedzi==4):
                wynik+=1
    return wynik