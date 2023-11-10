n = int(input())
list = []
if n == 1:
    print(1)
if n > 3:
    for i in range(1, n + 1):
        if i % 2 == 0:
            list.append(i)
    for j in range(1, n + 1):
        if j % 2 != 0:
            list.append(j)
    print(" ".join(map(str, list)))
else:
    print("NO SOLUTION")
