def number_spiral(y, x):
    z = max(y, x)
    d = z * (z - 1) + 1
    if z % 2 == 0:
        return d + y - x
    else:
        return d - y + x


t = int(input())
for _ in range(t):
    y, x = map(int, input().split())
    print(number_spiral(y, x))
