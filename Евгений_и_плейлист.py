n, m = map(int, input().split())
playlist = []

for i in range(n):
    c, t = map(int, input().split())
    playlist.append(c * t)
i = p = 0
for v in [int(x) for x in input().split()]:
    while p < v:
        p, i = p + playlist[i], i + 1
    print(i)
