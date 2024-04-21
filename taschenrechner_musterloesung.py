from cs50 import get_float, get_int


def main():
    while True:
        print("Bitte geben Sie die erste Zahl ein:")
        zahl1 = zahl_abfragen()
        print("Bitte geben Sie die zweite Zahl ein:")
        zahl2 = zahl_abfragen()

        ergebnis = 0
        operation = rechenart_abfragen()

        if operation == 1:
            ergebnis = addieren(zahl1, zahl2)
        elif operation == 2:
            ergebnis = subtrahieren(zahl1, zahl2)
        elif operation == 3:
            ergebnis = multiplizieren(zahl1, zahl2)
        elif operation == 4:
            ergebnis = dividieren(zahl1, zahl2)

        print(f"Ergebnis: {ergebnis}")

        print("Wollen Sie weitere Berechnungen durchführen? Gebe 1 für ja, 0 für nein! ")
        end_game = zahl_abfragen()
        if end_game == 0:
            break

    return


def addieren(zahl1, zahl2):
    return zahl1 + zahl2


def subtrahieren(zahl1, zahl2):
    return zahl1 - zahl2


def multiplizieren(zahl1, zahl2):
    return zahl1 * zahl2


def dividieren(zahl1, zahl2):
    return zahl1 / zahl2


def zahl_abfragen():
    return get_float("Eingabe: ")


def rechenart_abfragen():
    operation = 0
    while operation not in [1, 2, 3, 4]:
        operation = get_int("Was möchten Sie tun:\n1: addieren\n2: subtrahieren\n3: multiplizieren\n4: dividieren\n")
        if operation not in [1, 2, 3, 4]:
            print("Fehlerhafte Eingabe, bitte wähle 1, 2, 3 oder 4!")
        else:
            return operation


if __name__ == "__main__":
    main()
