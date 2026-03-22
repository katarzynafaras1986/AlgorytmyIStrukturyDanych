# 4. Napisz funkcję usuwającą i-ty węzeł z listy (węzły numerujemy od 1).

def remove_element(arr, element_number):
    for i in range(len(arr)):
        if i == element_number -1:
            del arr[i]
    print(arr)

remove_element([1,2,3,4,5,6,7,8,9,3], 2)
