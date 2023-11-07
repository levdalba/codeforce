n = int(input().strip())
count = 0

for _ in range(n):
    s = input().strip()
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if len(stack) == 0:
        count += 1

print(count)
