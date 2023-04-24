def policz_studentow(studenci) -> int:
    studenci = filter(lambda x: (str(x)).isnumeric() == False, studenci)
    liczba_studentow = len(list(studenci))
    print("Liczba studentow wynosi: " + str(liczba_studentow))
    return liczba_studentow