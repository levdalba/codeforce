q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    count = 0
    for x in a:
        if x % 2 == 1:
            count += 1

    if count < k or (count - k) % 2 == 1:
        print("NO")
    else:
        print("YES")
        j = 0
        for i in range(k - 1):
            while a[j] % 2 == 0:
                j += 1
            print(j + 1, end=" ")
            j += 1
        print(n)
