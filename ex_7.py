# zbadaj kazdy wykres, czy dla wyznaczonych punktow istnieje funkcja
# liniowa laczaca punkty
# jesli sie nie da, to zwroc False
# jesli sie da, zwroc True

def wykres(wykres) -> bool:
    if len(wykres) < 2:
        return False

    x1, y1 = wykres[0]
    x2, y2 = wykres[1]
    if x2 - x1 == 0:
        slope = None
    else:
        slope = (y2 - y1) / (x2 - x1)

    for i in range(2, len(wykres)):
        x1, y1 = wykres[i - 1]
        x2, y2 = wykres[i]
        if x2 - x1 == 0:
            if slope is not None:
                return False
        elif slope is None or (y2 - y1) / (x2 - x1) != slope:
            return False
    return True
