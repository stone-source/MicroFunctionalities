#3. Napisz skrypt do obliczania pierwiastków równania kwadratowego: ax^2+bx+c = 0

import math

class CRownianieKwadratowe:
    def __wyliczdelte(self):
        # delta = b^2 - 4ac
        return pow(self._B, 2) - (4 * self._A * self._C)
    def __wyliczx1(self):
        # x1 = -b-sqrt(delta)/2a
        return (-self._B-math.sqrt(self._Delta))/(2*self._A)
    def __wyliczx2(self):
        # x2 = -b+sqrt(delta)/2a
        return (-self._B+math.sqrt(self._Delta))/(2*self._A)
    def __wyliczx0(self):
        # x0 = -b/2a
        return -self._B/(2*self._A)
    def __init__(self, p_a, p_b, p_c):
        self._A = p_a
        self._B = p_b
        self._C = p_c
        self._Delta = self.__wyliczdelte()
    def wylicz(self):
        delta = self.__wyliczdelte()
        if delta < 0:
            print("Równanie kwadratowe nie ma żadnego rozwiązania.")
        elif delta == 0:
            print("Rozwiązaniem równania jest liczba: x = " + str(self.__wyliczx0()))
        else:
            print("Rozwiązaniami równania są liczby: x = " + str(self.__wyliczx1()) + " oraz x = " + str(self.__wyliczx2()))

def wprowadzliczbe(p_parametr, p_czyzero):
    while True:
        podanaliczba = input("Podaj " + p_parametr + ": ")
        try:
            val = int(podanaliczba)
            if p_czyzero and (val == 0):
                print("Podana liczba musi być różna od 0")
            else:
                return val
        except ValueError:
            print("Podana liczba jest nieprawidłowa")

if __name__ == '__main__':
    print("y = a^2 + bx + c = 0")
    a = wprowadzliczbe("A", True)
    b = wprowadzliczbe("B", False)
    c = wprowadzliczbe("C", False)

    rownanie = CRownianieKwadratowe(a, b, c)
    rownanie.wylicz()