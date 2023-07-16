'''Odejmoanie, mnozenie, dzielenie (ich definicje) z zadania 1'''
def odejmowanie(a, b):
    return (a[0] * b[1] - b[0] * a[1], a[1] * b[1])

def mnozenie(a, b):
    return (a[0] * b[0], a[1] * b[1])

def dzielenie(a, b):
    if b[0] == 0:
        return None
    return (a[0] * b[1], a[1] * b[0])


def uklad2na2(wsp_x_1, wsp_x_2, wsp_y_1, wsp_y_2, wart_1, wart_2):
    W = odejmowanie(mnozenie(wsp_x_1, wsp_y_2), mnozenie(wsp_x_2, wsp_y_1))
    Wx = odejmowanie(mnozenie(wsp_y_1, wart_2), mnozenie(wsp_y_2, wart_1))
    Wy = odejmowanie(mnozenie(wsp_x_1, wart_2), mnozenie(wsp_x_2, wart_1))
    if W[0] == 0 and Wx[0] == 0 and Wy[0] == 0:
        return "Układ nieoznaczony"
    elif (Wx[0] != 0 or Wy[0] != 0) and W[0] == 0:
        return "Układ sprzeczny"
    else:
        x = dzielenie(Wx, W)
        y = dzielenie(Wy, W)
        return "x=" + str(x) + "\n" + "y=" + str(y)


print(uklad2na2((1, 8), (1, 5), (4, 3), (1, 4), (7, 5), (3, 6)))
