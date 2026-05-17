# Zadanie 1. Rekurencja
# Zaimplementuj funkcję rekurencyjną power(base, exponent), która oblicza base^exponent (czyli
# base podniesione do potęgi exponent). Warunki:
# • Nie używaj operatora ** ani funkcji pow().
# • Zastosuj następującą zależność:
# o power(a, 0) = 1
# o power(a, n) = a * power(a, n-1) dla n > 0

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

if __name__ == '__main__':
    print(power(2, 3))
    print(power(2, 0))
    print(power(2, 5))