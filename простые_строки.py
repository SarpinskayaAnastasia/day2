s = input()
n = len(s)
for i in range(1, n):
    if s[i] == s[i - 1]:
        a = set(list(range(97, 123)))
        b = ('?' if i == n - 1 else s[i + 1])
        c = {ord(s[i]), ord(b)}
        a = a - c
        s = s[:i] + chr(a.pop()) + s[i + 1:]
print(s)
