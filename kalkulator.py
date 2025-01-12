def kalkulator():
    print("Prosty kalkulator")
    print("Dostępne operacje: +, -, *, /")
    x = float(input("Podaj pierwszą liczbę: "))
    operacja = input("Podaj operację: ")
    y = float(input("Podaj drugą liczbę: "))
    if operacja == "+":
        wynik = x + y
    elif operacja == "-":
        wynik = x - y
    elif operacja == "*":
        wynik = x * y
    elif operacja == "/":
        wynik = x / y
    else:
        print("Nieznana operacja!")
        return
    print(f"Wynik: {wynik}")

kalkulator()