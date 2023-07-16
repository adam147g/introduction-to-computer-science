# zadanie 4
# skoczek to KOŃ szachowy
# algorytm z powrotami

stop = False
wymiar = int(input('Napisz jak dużą szachownicę chcesz mieć: '))
startowy_wiersz=int(input('Napisz z jakiego wiersza chcesz startować: '))
startowa_kolumna=int(input('i jakiej kolumny: '))
print("")

szachownica = [[0 for _ in range(wymiar)] for _ in range(wymiar)]

def skoczek(szachownica, wymiar, obecny_wiersz, obecna_kolumna, poz=1):
    global stop

    if stop:
        return
    szachownica[obecny_wiersz][obecna_kolumna] = poz

    if poz == (wymiar ** 2):
        wypisz_szachownica(szachownica, wymiar)
        stop = True
        # exit(0) -> zastępstwo linijki: 5, 11 i 17 ,wyjście z funkcji

    for i in range(8):      # 8, bo jest 8 możliwych ruchów koniem w szachach
        x = spr(szachownica, wymiar, i, obecny_wiersz, obecna_kolumna)
        if x is not None:
            skoczek(szachownica, wymiar, x[0], x[1], poz + 1)
    szachownica[obecny_wiersz][obecna_kolumna] = 0  # wycofanie skoczka w momencie, gdyby był błąd



def wypisz_szachownica(tab, wymiar):

    for i in range(wymiar):
        for j in range(wymiar):
            print(tab[i][j], end="\t")
        print("")
    print("")
    # input() -> tego bym użył bez linijek: 5, 11, 17 i 18, żeby mi
    # wypisywało po wciśnięciu enter'a kolejne możliwe takie tablice skoczka


# teraz definiujemy funkcję sprawdzającą, czy da się w jakieś
# miejsce wykonać ruch skoczkiem (koniem)

def spr(szachownica, wymiar, i, obecny_wiersz, obecna_kolumna):

    ruch_w = [2, 1, -1, -2, -2, -1, 1, 2]  # ruch wierszem
    ruch_k = [1, 2, 2, 1, -1, -2, -2, -1]  # ruch kolumną
    nowy_w = obecny_wiersz + ruch_w[i]
    nowa_k = obecna_kolumna + ruch_k[i]
    if 0 <= nowy_w < wymiar and 0 <= nowa_k < wymiar and szachownica[nowy_w][nowa_k] == 0:
        return (nowy_w, nowa_k)
    return None


skoczek(szachownica, wymiar, startowy_wiersz, startowa_kolumna)
