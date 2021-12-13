for _ in range(int(input())):
    answer = 0
    for i in range(2):
        n = int(input())
        r = list(map(int, input().split(' ')))
        for j in range(1, n):
            r[j] += r[j - 1]
        answer += max(0, max(r))
    print(answer)
