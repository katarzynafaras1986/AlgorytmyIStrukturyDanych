# Zadanie 5. Programowanie dynamiczne
# Masz zestaw nominałów monet [1, 3, 4] i kwotę 6. Znajdź minimalną liczbę monet potrzebnych do
# osiągnięcia tej kwoty. Wskazówka: Stwórz tablicę dp[i], gdzie dp[i] to minimalna liczba monet, by
# uzyskać sumę i.

def min_coins(coins, amount):
    # duża liczba oznaczająca brak rozwiązania
    INF = float('inf')

    # tablica DP
    dp = [INF] * (amount + 1)

    # aby uzyskać kwotę 0 potrzeba 0 monet
    dp[0] = 0

    # obliczanie minimalnej liczby monet
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]


# przykład użycia
coins = [1, 3, 4]
amount = 6

print(min_coins(coins, amount))  # wynik: 2