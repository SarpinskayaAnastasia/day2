n, b = map(int, input().split())
a = list(map(int, input().split()))
bit = []
o, e = 0, 0
if a[0] % 2 == 0:
    o += 1
else:
    e += 1
for result in range(1, n - 1):
    if a[result] % 2 == 0:
        o += 1
    else:
        e += 1
    if o == e:
        bit.append(abs(a[result + 1] - a[result]))
bit.sort()
result = 0
while result < len(bit) and bit[result] <= b:
    b -= bit[result]
    result += 1
print(result)
