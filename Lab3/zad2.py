# Zadanie 2.
# Napisz program czytający wyrażenie arytmetyczne w notacji postfiksowej (Odwrotna Notacja Polska)
# i obliczający jego wartość z wykorzystaniem stosu.
# ONP (ang. RPN - Reverse Polish Notation) jest sposobem zapisu wyrażeń arytmetycznych bez
# stosowania nawiasów, w którym symbol operacji występuje po argumentach. Poniżej podajemy
# przykłady wyrażeń w ONP:
# Notacja normalna ONP
# 2 + 2 = 2 2 + =
# 3 + 2 * 5 = 3 2 5 * + =
# 2 * (5 + 2) = 2 5 2 + * =
# (7 + 3) * (5 - 2) ^ 2 = 7 3 + 5 2 - 2 ^ * =
# 4 / (3 - 1) ^ (2 * 3) = 4 3 1 - 2 3 * ^ / =
# Algorytm obliczania wartości wyrażenia ONP wykorzystuje stos do składowania wyników pośrednich.
# Zasada pracy tego algorytmu jest bardzo prosta:
# Z wejścia odczytujemy kolejne elementy wyrażenia. Jeśli element jest liczbą, zapisujemy ją na stosie.
# Jeśli element jest operatorem, ze stosu zdejmujemy dwie liczby, wykonujemy nad nimi operację
# określoną przez odczytany element, wynik operacji umieszczamy z powrotem na stosie. Jeśli element
# jest końcowym znakiem '=', to na wyjście przesyłamy liczbę ze szczytu stosu i kończymy. Inaczej
# kontynuujemy odczyt i przetwarzanie kolejnych elementów.
# Przykładowo obliczmy tą metodą wartość wyrażenia 7 3 + 5 2 - 2 ^ * =
# we stos wy
# 7 7
# 3 7 3
# + 10
# 5 10 5
# 2 10 5 2
# - 10 3
# 2 10 3 2
# ^ 10 9
# * 90
# = 90
import re

def onp(wyrazenie):
    stos = []
    result = wyrazenie.split()
    print(result)

    for znak in result:
        if znak.isnumeric():
            stos.append(int(znak))
        elif not znak.isnumeric():
            if znak == "=":
                print(stos.pop())
                break
            else:
                a = stos.pop()
                b = stos.pop()
            if znak == "+":
                stos.append(a + b)
            elif znak == "-":
                stos.append(b - a)
            elif znak == "*":
                stos.append(a * a)
            elif znak == "/":
                stos.append(b / a)
            elif znak == "^":
                stos.append(b ** a)



if __name__ == "__main__":
    onp("2 3 ^ = ")