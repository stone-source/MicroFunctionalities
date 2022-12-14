#1. Napisz skrypt obliczający silnię dowolnej liczby;

def wylicz_silnia(n):
    if n > 1:
        return n*wylicz_silnia(n-1)
    return 1

if __name__ == '__main__':
    print(str(wylicz_silnia(3)))
