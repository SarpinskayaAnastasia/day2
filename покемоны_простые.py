for _ in " " * int(input()):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    answer, flag = 0, 0
    for i in range(1, n):
        if flag == 0:
            if a[i] < a[i - 1]:
                answer += a[i - 1]
                flag += 1
        else:
            if a[i] > a[i - 1]:
                answer -= a[i - 1]
                flag -= 1
    print(answer if flag else answer + a[-1])
