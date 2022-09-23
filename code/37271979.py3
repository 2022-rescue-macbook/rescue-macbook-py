from sys import stdin
num = int(stdin.readline())

for i in range(num):
    data = list(map(int, stdin.readline().split()))
    printer = list(map(int, stdin.readline().split()))
    if data[0] == 1:
        print(1)

    elif len(set(printer)) == len(printer) or printer.count(printer[data[1]]) == 1:
        print(sorted(printer, reverse=True).index(printer[data[1]]) + 1)

    else:
        find_arr = ["false"] * data[0]
        find_arr[data[1]] = "true"
        cnt = 0
        while(1):
            if "true" not in find_arr:
                print(cnt)
                break
                
            large = max(printer)
            if len(set(printer)) == 1:
                print(find_arr.index("true") + 1 + cnt)
                break
            else:
                temp = printer.index(large)
                printer = printer[temp + 1:] + printer[:temp]
                find_arr = find_arr[temp + 1 :] + find_arr[:temp]
                cnt += 1








