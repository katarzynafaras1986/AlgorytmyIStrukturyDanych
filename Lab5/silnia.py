def silnia(n):
    if n == 0 or n == 1: # przypadek bazowy
         return 1
    return n * silnia(n - 1)