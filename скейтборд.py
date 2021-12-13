s = input()
answer = 0
for symbol in s:
    answer += int(symbol) % 4 == 0
for i in range(len(s) - 1):
    answer += (int(s[i:i + 2]) % 4 == 0) * (i + 1)
print(answer)
