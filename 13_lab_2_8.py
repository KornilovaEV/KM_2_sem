number = int(input())
i = 1
result = 0
while i < number:
    i = i * 2
    if i == number:
        result = 1
    else:
        result = 0
if result == 1:
    print("YES")
else:
    print("NO")