# dana jest lista liczb
# wstawiamy je do kolejki
# zdejmujemy je i wpisujemy parzyste

from collections import deque

if __name__ == "__main__":
    liczby = [3, 8, 5, 3, 5, 9]

    kolejka = deque()

    for x in liczby:
        kolejka.append(x)

        while kolejka:
            element = kolejka.popleft()

            if element % 2 == 0:
                print(element)
