# 6. Napisz funkcję zapisującą do listy liczby w taki sposób, aby w każdym momencie działania
# programu lista była posortowana.
def insert_sorted(arr, value):
    i = 0

    while i < len(arr) and arr[i] < value:
        i += 1

    arr.insert(i, value)


if __name__ == "__main__":
    arr = []

    insert_sorted(arr, 5)
    insert_sorted(arr, 2)
    insert_sorted(arr, 8)
    insert_sorted(arr, 4)
    insert_sorted(arr, 1)

    print(arr)
