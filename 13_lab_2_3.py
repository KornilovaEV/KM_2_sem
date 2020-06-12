def merge(left, right):
    lst = []
    while left and right:
        if left[0] < right[0]:
            lst.append(left.pop(0))
        else:
            lst.append(right.pop(0))
    if left:
        lst.extend(left)
    if right:
        lst.extend(right)
    return lst

def mergesort(lst):
    length = len(lst)
    if length >= 2:
        сentre = int(length / 2)
        lst = merge(mergesort(lst[:сentre]), mergesort(lst[сentre:]))
    return lst


try:
    n = list(input())
    print(mergesort(n))
except ValueError:
    print('Opssss, error')

