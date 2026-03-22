# 5. Napisz funkcję scalającą (merge) dwie uporządkowane listy w jedną uporządkowana listę.

def merge(arr1, arr2):
    """
    Merge two sorted arrays
    :param arr1:
    :param arr2:
    :return:
    """
    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] < arr2[0]:
            arr1.pop(0)
            arr2[]

