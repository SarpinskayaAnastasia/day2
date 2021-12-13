n, q, k = map(int, input().split())
a = list(map(int, input().split()))
for _ in range(q):
    l, r = map(int, input().split())
    res = k + a[r - 1] - a[l - 1] - 2 * (r - l) - 1
    print(res)
