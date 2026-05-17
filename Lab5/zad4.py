# Zadanie 4. Programowanie dynamiczne
# Masz plecak o pojemności 𝑊 i zestaw 𝑛 przedmiotów. Każdy przedmiot ma wagę 𝑤[𝑖] i wartość 𝑣[𝑖].
# Wybierz przedmioty tak, by maksymalizować wartość bez przekraczania pojemności. Informacje
# odnośnie problemu plecakowego można znaleźć pod adresem
# https://pl.wikipedia.org/wiki/Problem_plecakowy

def knapsack(W, weights, values, n):
    # tworzenie tablicy DP
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # wypełnianie tablicy
    for i in range(1, n + 1):
        for w in range(W + 1):

            # jeśli przedmiot mieści się w plecaku
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# przykład użycia
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5
n = len(weights)

print(knapsack(W, weights, values, n))  # wynik: 7