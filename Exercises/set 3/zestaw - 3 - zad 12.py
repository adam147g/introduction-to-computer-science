from random import randint


def zad12(tab):
    l_tab = len(tab)
    licz_D, licz_U, licz_max_D, licz_max_U, pom1, pom2 = 2, 2, 2, 2, 0, 0
    for i in range(l_tab - 2):
        r = tab[i + 1] - tab[i]
        if r > 0:
            if (tab[i + 2] - tab[i + 1]) == r:
                licz_D += 1
            else:
                if licz_D > licz_max_D:
                    licz_max_D = licz_D
                    licz_D = 2
            pom1 = 1
        elif r < 0:
            if (tab[i + 2] - tab[i + 1]) == r:
                licz_U += 1
            else:
                if licz_U > licz_max_U:
                    licz_max_U = licz_U
                    licz_U = 2
            pom2 = 1


    if pom1 == 0:
        return (licz_max_U, "Występują tylko ciągi ujemne, a najdłuższy z nich o długości wskazanej")
    elif pom2 == 0:
        return (licz_max_D, "Występują tylko ciągi dodatnie, a najdłuższy z nich o długości wskazanej")
    else:
        x = (licz_max_D - licz_max_U)
        if x > 0:
            return (x, "Na korzyść dodatnich")
        elif x == 0:
            return (x, "Ciągi są równe co do długości")
        else:
            return (-x, "Na korzyść ujemnych")


t = list()
N = 10
i = 0
while i < N:
    x = randint(1, 100)
    if x % 2 == 1:
        t.append(x)
        i += 1
    else:
        continue
print(t)
print(zad12(t))


'''def the_longest_sequence():
    t = list()
    N = 100
    i = 1
    j = 1
    lastDifference = 1
    longestIncreasing = 1
    longestDecreasing = 1
    currentSequenceLength = 1
    for i in range(N):
        x = randint(1, N)
        if x not in t and x % 2 == 1:
            t.append(x)
        else:
            i -= 1
    print(t)
    while j < len(t):
        currentDifference = t[j] - t[j-1]
        if currentDifference == lastDifference:
            currentSequenceLength += 1
        else:
            currentSequenceLength = 2
            lastDifference = currentDifference
        if lastDifference > 0:
            longestIncreasing = max(longestIncreasing, currentSequenceLength)
        elif lastDifference < 0:
            longestDecreasing = max(longestDecreasing, currentSequenceLength)
        j += 1
        result = longestIncreasing - longestDecreasing
    return result

print(the_longest_sequence())'''
