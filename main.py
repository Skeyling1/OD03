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
    elenent = s[0]
    left = []
    cenrte = []
    right = []
   # left = lambda
