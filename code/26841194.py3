

def solution(n, m, data):
    cnt = 0
    mx = max(data)
    data_list = list()
    for i in range(0, len(data)):
        data_list.append((i, data[i]))
    isFind = True
    while isFind:
        mx = max(data)
        for tu in data_list:
            if tu[1] == mx:
                cnt += 1
                if m == tu[0]:
                    isFind = False
                    break
                else:
                    data.remove(tu[1])
                    data_list.remove(tu)
                    break
            else:
                tmp = tu;
                data_list.remove(tu)
                data_list.append(tmp)
                break
    print(cnt)

def main():
    case = int(input())
    for i in range(0, case):
        n, m = list(map(int, input().split(' ')))
        data = list(map(int, input().split(' ')))
        solution(n, m, data)


if __name__ == "__main__":
    main()