# Policz studentki i studentow i zwroc wynik w formacie: [k, m]
# Przyjmij, ze imie dla kobiety konczy sie na "a"
def policz_studentow_plec(studenci):
    liczba_mezczyzn = 0
    liczba_kobiet = 0
    for name in studenci:
        if name[-1] == 'a':
            liczba_kobiet += 1
        else:
            liczba_mezczyzn += 1

        return[liczba_kobiet, liczba_mezczyzn]
    studenci = []
    result = policz_studentow_plec(studenci)
    print(result)

