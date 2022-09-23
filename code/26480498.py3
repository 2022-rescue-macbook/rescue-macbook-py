def solution2(list, index):
    chk = [0 for index in range(len(list))]
    chk[index] = 1
    num = 1
    while len(list) != 0:
        if list[0] == max(list):
            list.pop(0)
            if chk.pop(0) == 1:
                return str(num)
            num += 1
        else:
            list.append(list.pop(0))
            chk.append(chk.pop(0))

result = []
for i in range(int(input())):
    case, index = map(int, input().split(' '))
    lists = list(map(int, input().split(' ')))

    result.append(solution2(lists, index))

print('\n'.join(result))

# list = [1, 1, 9, 1, 1, 1]



