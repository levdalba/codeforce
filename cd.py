def min_blows(n, x, blows):
    max_d = max_h = -1
    for d, h in blows:
        max_d = max(max_d, d)
        max_h = max(max_h, d - h)
    if max_d >= x:
        return 1
    if max_h <= 0:
        return -1
    return (x - max_d + max_h - 1) // max_h + 1


t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    blows = [tuple(map(int, input().split())) for j in range(n)]
    print(min_blows(n, x, blows))
