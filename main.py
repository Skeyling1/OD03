# Пузырьковая сортировка
def bubble(s):
    for run in s:
        for i in s:
            if i > i+1:
                run[i], run[i+1] = run[i+1], run[i]
