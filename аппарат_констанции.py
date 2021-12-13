input_string = input()
if 'm' in input_string or 'w' in input_string:
    print(0)
    exit()
answer = [1]
for index, elem in enumerate(input_string):
    if (elem != 'n' and elem != 'u') or (not index) or (input_string[index - 1] != elem):
        answer.append(answer[-1])
    else:
        answer.append((answer[-1] + answer[-2]) % (10 ** 9 + 7))
print(answer[-1])
