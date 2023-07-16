"""
Dana jest tablica T[N] zawierająca oporności N rezystorów wyrażonych całkowitą liczbą kΩ.
Proszę napisać funkcję, która sprawdza czy jest możliwe uzyskanie wypadkowej rezystancji
R (równej całkowitej liczbie kΩ) łącząc dowolnie 3 wybrane rezystory.
"""


def check(T, R, res):
    if abs(T[res[0]] + T[res[1]] + T[res[2]]) == R:
        return True
    r1_and_r2_and_r3 = T[res[0]] * T[res[1]] + T[res[0]] * T[res[2]] + T[res[1]] * T[res[2]]
    if abs((T[res[0]] * T[res[1]] * T[res[2]]) / r1_and_r2_and_r3) == R:
        return True
    r1_and_r2 = (T[res[0]] * T[res[1]]) / (T[res[0]] + T[res[1]])
    if abs(r1_and_r2 + T[res[2]]) == R:
        return True
    r1_and_r3 = (T[res[0]] * T[res[2]]) / (T[res[0]] + T[res[2]])
    if abs(r1_and_r3 + T[res[1]]) == R:
        return True
    r2_and_r3 = (T[res[1]] * T[res[2]]) / (T[res[1]] + T[res[2]])
    if abs(r2_and_r3 + T[res[0]]) == R:
        return True
    if abs(T[res[0]] * (T[res[1]] + T[res[2]]) / (T[res[0]] + T[res[1]] + T[res[2]])) == R:
        return True
    if abs(T[res[1]] * (T[res[0]] + T[res[2]]) / (T[res[0]] + T[res[1]] + T[res[2]])) == R:
        return True
    if abs(T[res[2]] * (T[res[0]] + T[res[1]]) / (T[res[0]] + T[res[1]] + T[res[2]])) == R:
        return True
    return False


def check_resistance(T, R, index, resistors_number, actual_resistors):
    if resistors_number == 3:
        return check(T, R, actual_resistors)
    if index == len(T):
        return False
    actual_resistors.append(index)
    if check_resistance(T, R, index + 1, resistors_number + 1, actual_resistors):
        return True
    actual_resistors.remove(index)
    if check_resistance(T, R, index + 1, resistors_number, actual_resistors):
        return True
    return False


def resistance(T, R):
    return check_resistance(T, R, 0, 0, [])


T = [11, 19, 6, 8, 4, 17, 2, 15, 1, 3]
print(resistance(T, 14))