# 3. Napisz funkcję wyszukującą na liście podaną wartość.

def find_value(arr, value):
    arr2 = []

    for i in range(len(arr)):
        if arr[i] == value:
            arr2.append(i)

    print("Value found on index: ", arr2)


find_value([1,2,3,4,5,6,7,8,9,3], 3)

