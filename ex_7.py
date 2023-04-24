# zbadaj kazdy wykres, czy dla wyznaczonych punktow istnieje funkcja
# liniowa laczaca punkty
# jesli sie nie da, to zwroc False
# jesli sie da, zwroc True

def wykres(dane) -> bool:
    if len(dane) < 2:
        return False
    slope = [dane[1][0] - dane[0][0], dane[1][1] - dane[0][1]]
    for i in range(1, len(dane)):
        if [dane[i][0] - dane[i-1][0], dane[i][1] - dane[i-1][1]] != slope:
            return False
    return True