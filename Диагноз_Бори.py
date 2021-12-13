result = 0
for i in range(int(input())):
    s, d = map(int, input().split())
    if result < s:
        result = s
    else:
        result = s + ((result - s) // d + 1) * d
print(result)
