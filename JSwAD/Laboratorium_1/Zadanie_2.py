#2. Gra za dużo/za mało

import random

#Global
g_LibaProb = 0

#Msg
c_Msg_BlednaLiczba = "Błędna liczba. Podaj wartość z zakresu 0-1000"

def zgaduje_liczbe(p_WylosowanaLiczba):
    while True:
        global g_LibaProb
        g_LibaProb += 1
        podanaLiczba = input("Zgadnij wylosowaną liczbę: ")
        try:
            val = int(podanaLiczba)

            if (val >= 0) and (val <= 1000):
                if wylosowanaLiczba == val:
                    print("Trafiłeś!")
                    print("Liczba prób: " + str(g_LibaProb))
                    return True
                elif wylosowanaLiczba < val:
                    print("Za dużo...")
                    return False
                else:
                    print("Za mało...")
                    return False
                break
            else:
                print(c_Msg_BlednaLiczba)

        except ValueError:
            print(c_Msg_BlednaLiczba)

if __name__ == '__main__':
    wylosowanaLiczba = random.randint(0, 1000)
    print("Program losuje liczbę z zakresu 0-1000")
    while True:
        if zgaduje_liczbe(wylosowanaLiczba):
          break