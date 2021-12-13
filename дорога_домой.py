for _ in range(int(input())):
    a, b, p = map(int, input().split())
    string = input()
    length = len(string)
    result = len(string)
    for i in range(length - 2, -1, -1):
        if string[i] != string[i + 1] or i == length - 2:
            if string[i] == "A":
                p -= a
            else:
                p -= b
        if p >= 0:
            result -= 1
        else:
            break
    print(result)
