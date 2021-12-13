import bisect

input()
x = list(sorted(map(int, input().split())))
q = int(input())
for i in range(q):
    m = int(input())
    print(bisect.bisect_right(x, m))
