n = int(input())
ans = []
while n > 1:
    x = n // 2
    ans.append(x)
    n -= x

ans.reverse()
print(len(ans))
print(*ans)
