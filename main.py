# Пузырьковая сортировка
def bubble(s):
    for run in range(len(s)):
        for i in range(len(s)-1-run):
            if s[i] > s[i+1]:
                s[i], s[i+1] = s[i+1], s[i]
    return s


s = [9, 6, 4, 3, 1, 2]

print(bubble(s))


# fast sorting
def fast_sort(s):
    if len(s) <= 1:
        return s # условие выхода: если длина списка будет меньше или равна 1
    element = s[0]
    left = list(filter(lambda i: i < element, s))
    centre = [i for i in s if i == element]#генератор списков
    right = list(filter(lambda i: i > element, s))
    return fast_sort(left) + centre + fast_sort(right)#Добавим рекурсию


gf = [5, 3, 5, 2, 6, 8, 9, 6, 5, 4, 5, 8]
print(fast_sort(gf))


#Сортировка выбором
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j  # меняем местами при том, что j меньше.
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


dd = [-3, 4, -6, 8, 1, 8, -2]
print(selection_sort(dd))


# Сортировка вставками
def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

ddd = [-3, 4, -6, 8, 1, 8, -2, 2, -9]
insert_sort(ddd)
print(ddd)