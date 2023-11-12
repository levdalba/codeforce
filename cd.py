n = int(input())
for k in range(1, n + 1):
    total_positions = k * k
    total_ways = total_positions * (total_positions - 1) // 2
    attacking_ways = 4 * (k - 1) * (k - 2)
    print(total_ways - attacking_ways)
