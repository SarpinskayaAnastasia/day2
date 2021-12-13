s = ''
array = [0]
for i in input():
    array.append(array[-1] + (1 if s == i else 0))
    s = i
for _ in range(int(input())):
    l, r = map(int, input().split())
    print(array[r] - array[l])
