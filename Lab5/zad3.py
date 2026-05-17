# Zadanie 3. Rekurencja + memoizacja
# Dana jest lista dostępnych nominałów monet oraz kwota do rozmienienia. Napisz funkcję
# count_ways(coins, amount), która oblicza liczbę unikalnych sposobów rozmienienia danej kwoty z
# użyciem dostępnych monet (każdą monetę można użyć dowolną liczbę razy). Wykorzystaj rekurencję
# z memoizacją, aby przyspieszyć obliczenia. Przykład:
# coins = [1, 2, 5]
# amount = 5
# count_ways(coins, 5) → 4
# Możliwe kombinacje:
# • 1+1+1+1+1
# • 1+1+1+2
# • 1+2+2
# • 5

def count_ways(coins, amount):
    memo = {}

    def helper(index, remaining):
        # jeśli dokładnie rozmieniono kwotę
        if remaining == 0:
            return 1

        # jeśli kwota jest ujemna lub brak monet
        if remaining < 0 or index == len(coins):
            return 0

        # sprawdzenie memoizacji
        if (index, remaining) in memo:
            return memo[(index, remaining)]

        # używamy monety lub przechodzimy do następnej
        use_coin = helper(index, remaining - coins[index])
        skip_coin = helper(index + 1, remaining)

        memo[(index, remaining)] = use_coin + skip_coin
        return memo[(index, remaining)]

    return helper(0, amount)


# przykład użycia
coins = [1, 2, 5]
amount = 5

print(count_ways(coins, amount))  # wynik: 4