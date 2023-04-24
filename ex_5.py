# Oblicz liczbę nawiasów w zmiennej, zwroc: [otwierajace, zamykajace]

def nawiasy(tekst: str) -> [int, int]:
    nawasiasy_otwieraj = tekst.count("[")
    nawiasy_zamykaj = tekst.count("]")
    return [nawasiasy_otwieraj, nawiasy_zamykaj]