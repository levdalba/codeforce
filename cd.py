s = input().strip()
open = close = count = 0

for i in range(len(s) - 1, -1, -1):
    if s[i : i + 2] == "))":
        close += 1
    elif s[i : i + 2] == "((":
        count += close

print(count)
