# 2. Zaimplementuj algorytm przesuwający elementy tablicy w lewo lub w prawo o zadany krok k.


def przeszun_element(arr, krok, kierunek):
    """

    :param arr:
    :param krok:
    :param kierunek:
    :return:
    """

    print(arr[krok:] + arr[:krok]) if kierunek == 0 else print(arr[-krok:] + arr[:-krok])

przeszun_element([1,2,3,4,5], 1, 0)
przeszun_element([1,2,3,4,5], 2, 0)
przeszun_element([1,2,3,4,5], 1, 1)
przeszun_element([1,2,3,4,5], 2, 1)



