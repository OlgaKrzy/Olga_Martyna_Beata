# sprawdz, czy nawias ma swoja pare, jesli ma swroc True, jesli nie False

def para_nawiasow(tekst: str) -> bool:
    stos = []
    for znak in tekst:
        if znak == '(':
            stos.append('(')
        elif znak == ')':
            if len(stos) == 0 or stos[-1] != '(':
                return False
            stos.pop()
    return len(stos) == 0

