m, s = map(int, input().split())
if (s == 0 and m != 1) or s > 9 * m:
    print(-1, -1)
    exit()
a = (10 ** ((s - 1) // 9) * ((s - 1) % 9 + 1)) - 1 + 10 ** (m - 1)
b = (10 ** m) - (10 ** (m - (s - 1) // 9 - 1)) * (10 - (s - (s - 1) // 9 * 9))
print(int(a), int(b))
