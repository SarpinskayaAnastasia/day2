for _ in range(int(input())):
    s = input()
    if s.find('00', s.find('11')) < 0:
        print('YES')
    else:
        print('NO')
