n, k = map(int, input().split())
a = [*map(int, input().split())]
w = 0
for i in range(1, n):
    summand = abs(max(0, k - a[i] - a[i - 1]))
    w += summand
    a[i] += summand
print(w)
print(*a)
