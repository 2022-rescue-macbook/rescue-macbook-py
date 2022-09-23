num = int(input())

for x in range(num):
    n, k = map(int, input().split())
    data = list(map(int,input().split()))
    data_backup = data.copy()
    data_backup[k] = 0
    cnt = 0

    while data:
        if data[0] == max(data):
            cnt += 1
            if data_backup[0] == 0:
                print(cnt)
                break
            else:
                data.pop(0)
                data_backup.pop(0)
        else:
            data.append(data[0])
            data_backup.append(data_backup[0])
            del data[0]
            del data_backup[0]