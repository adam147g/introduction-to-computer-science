# Bit algo
# Podział kwoty na nominały (ilość tych podziałów)

def count(n,l,last):
    if n==0:
        return 1
    if n<0:
        return 0
    counter=0

    for i in l:
        if i>=last:
            counter+=count(n-i,l,i)

    return counter


l=[3,5,2]
n=15
print(count(n,l,-1))