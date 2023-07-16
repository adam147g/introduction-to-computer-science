"""
Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów
tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów
znalezionego podzbioru. Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10.
"""

# ?

def the_lowest_number(array, index=0, index_summary=0, value_number=0, subset_len=0):
    if index == len(array) - 1:
        if index_summary == value_number and subset_len != 0:
            return (subset_len, index_summary)
        else:
            return (len(array) + 1, -1)
    number1 = the_lowest_number(array, index + 1, index_summary, value_number, subset_len)
    number2 = the_lowest_number(array, index + 1, index_summary + array[index + 1], value_number + index + 1,subset_len + 1)
    if number1[0] < number2[0]:
        return number1
    else:
        return number2


array = [1, 7, 3, 5, 11, 2]
print(the_lowest_number(array))