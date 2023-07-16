"""
Napisać program wyznaczający na drodze eksperymentu prawdopodobieństwo tego, że w grupie N przypadkowo
spotkanych osób, co najmniej dwie urodziły się tego samego dnia roku. Wyznaczyć wartości
prawdopodobieństwa dla N z zakresu 20-40.
"""
# P = 1*(364/365)*(363/365)*(364/365)...
# Paradoks Dnia Urodzin
# https://www.wikiwand.com/pl/Paradoks_dnia_urodzin


def probability(index):
    count = 1
    for i in range(index):
        count *= (1 - i / 365)
    return 1 - count


def probability_of_being_born_same_day():
    start = 1
    while start <= 50:
        print(start," - ", probability(start)*100,"%")
        start += 1


probability_of_being_born_same_day()