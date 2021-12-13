def run(jhne):
    result = 0
    for i in range(len(jhne)):
        flag = False
        for j in jhne[i]:
            if j == '1':
                flag = True
            if j == '0' and flag is True:
                result += 1
    return result


n, m = map(int, input().split())
r = [''.join(input().split()) for i in range(n)]
line = [i[::-1] for i in r]
u = [''.join([i[j] for i in r]) for j in range(m)]
d = [i[::-1] for i in u]
print(run(line) + run(r) + run(u) + run(d))
