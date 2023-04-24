# Zaokraglij do dwoch miejsc po przecinku
def oblicz_potega(liczba, potega) -> float:
    wynik = pow(liczba, potega)
    wynik_zaokraglony = round(wynik, 2)
    return wynik_zaokraglony
