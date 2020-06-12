def leonardo(n):
    if n in (1, 2):
        return 1
    return leonardo(n - 1) + leonardo(n - 2) + 1
 
 
print(leonardo(20))

