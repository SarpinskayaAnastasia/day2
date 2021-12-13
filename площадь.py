for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    counter = 0
    for q in range(n):
        s = input()
        a = s.count("..")
        b = s.count(".")
        if y < 2 * x:
            counter += a * y + (b - 2 * a) * x
        else:
            counter += b * x
    print(counter)
