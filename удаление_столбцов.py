def remove(p, st):
    for aiter in range(len(st)):
        st[aiter] = st[aiter][:p] + st[aiter][p + 1:]


n, m = [int(x) for x in input().split()]
a = []
for i in range(n):
    a.append(input())
removed = 0
for i in range(m):
    i -= removed
    for j in range(n - 1):
        if a[j][:i + 1] > a[j + 1][:i + 1]:
            remove(i, a)
            removed += 1
            break
print(removed)
