# 5. Napisz funkcję scalającą (merge) dwie uporządkowane listy w jedną uporządkowana listę.

def merge(arr1, arr2):
    """
    Merge two sorted arrays.

    :param arr1: pierwsza posortowana lista
    :param arr2: druga posortowana lista
    :return: nowa posortowana lista
    """

    result = []

    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] < arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))

    while len(arr1) > 0:
        result.append(arr1.pop(0))

    while len(arr2) > 0:
        result.append(arr2.pop(0))

    return result


if __name__ == "__main__":
    print(merge([1, 3, 5], [2, 4, 6]))

