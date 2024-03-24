bok_a = 8
pole_kw = (bok_a)**2
print(pole_kw)

def pole_trapezu(a, b, h):
    return 0.5 * (a + b) * h

podstawa_a = 123
podstawa_b = 999
wysokosc = 89

wynik = pole_trapezu(podstawa_a, podstawa_b, wysokosc)
print("Pole trapezu wynosi:", wynik)

def oblicz_pole_trojkata(a, h):
    return a * h / 2

# Dane trójkąta
bok_a = 8
wysokosc = 5

# Obliczanie pola trójkąta i wyświetlanie wyniku
print("pole trójkąta wynosi:", oblicz_pole_trojkata(bok_a, wysokosc))


