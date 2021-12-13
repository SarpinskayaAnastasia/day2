for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    answer = 'YES'
    a = 0
    b = 0
    for i in range(n - 1):
        a += array[i]
        b += array[n - i - 1]
        if a < 1 or b < 1:
            answer = 'NO'
            break
    print(answer)
