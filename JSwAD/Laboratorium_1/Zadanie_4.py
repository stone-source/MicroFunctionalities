"""
4. Napisz skrypt żądający od użytkownika podania dwóch liczb całkowitych. Program powinien
   wyliczyć i podać sumę wszystkich liczb całkowitych pomiędzy podanymi liczbami.
"""

class CCalc:
    def __init__(self, p_l1, p_l2):
        self._l1 = min(p_l1, p_l2)
        self._l2 = max(p_l1, p_l2)

    def wylicz(self):
        val = 0
        iii = 0
        tmp = 0
        for x in range(self._l1, self._l2 + 1):
            iii += 1
            val += x
            print(str(iii) + ") " + str(tmp) + " + " + str(x) + " = " + str(val))
            tmp = val

        print("\nLiczba wykonanych kroków: " + str(iii))
        print("Suma liczb z zakresu od: >= " + str(self._l1) + " do: <= " + str(self._l2) + " wynosi = " + str(val))

def wprowadzliczbe():
    while True:
        podanaliczba = input("Podaj liczbę całkowitą:")
        try:
            val = int(podanaliczba)
            if val < 0:
                print("Podana liczba nie może być mniejsza od 0")
            else:
                return val
        except ValueError:
            print("Podana liczba jest nieprawidłowa")

if __name__ == '__main__':
    a = wprowadzliczbe()
    b = wprowadzliczbe()

    calc = CCalc(a, b)
    calc.wylicz()
