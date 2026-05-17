# Zadanie 2. Rekurencja
# Dana jest plansza 𝑛 𝑥 𝑚. Z punktu (0, 0) możesz poruszać się tylko w prawo lub w dół. Napisz funkcję
# rekurencyjną count_paths(n, m), która zwraca liczbę wszystkich możliwych ścieżek do punktu (𝑛 −
# 1, 𝑚 − 1). Zależność:
# • count_paths(1, m) = 1
# • count_paths(n, 1) = 1
# • count_paths(n, m) = count_paths(n-1, m) + count_paths(n, m-1)

def count_paths(n, m):
    # przypadki bazowe
    if n == 1 or m == 1:
        return 1

    # rekurencja
    return count_paths(n - 1, m) + count_paths(n, m - 1)


# przykład użycia
print(count_paths(3, 3))  # wynik: 6