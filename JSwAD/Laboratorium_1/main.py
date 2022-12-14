#3. Napisz skrypt do obliczania pierwiastków równania kwadratowego;

import enum

def wprowadz_liczbe(p_Parametr, p_NieMozeBycZerem):
    while True:
        podanaLiczba = input("Podaj " + p_Parametr + ": ")
        try:
            val = int(podanaLiczba)
            if p_NieMozeBycZerem and (val == 0):
                print("Podana liczba musi być różna od 0")
            else:
                return val
        except ValueError:
            print("Podana liczba jest nieprawidłowa")

if __name__ == '__main__':
    print("y = a^2 + bx + c = 0")
    a = wprowadz_liczbe("A", True)
    b = wprowadz_liczbe("B", False)
    c = wprowadz_liczbe("C", False)