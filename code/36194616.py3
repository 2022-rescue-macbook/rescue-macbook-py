import sys
temp = int(sys.stdin.readline())
for i in range(temp):
    loaction = 0
    count = 0
    N, M = map(int, sys.stdin.readline().split())
    file = list(map(int,sys.stdin.readline().split()))
    level = list(set(file))
    level.sort(reverse = True)
    if file[M] == level[0]:
        for j in file[:M+1]:
            if j == file[M]:
                count += 1
    else:
        location = len(file) - 1 - file[::-1].index(level[0]) # 가장 높은 중요도의 가장 오른쪽
        for k in level[1:level.index(file[M])]:
            if k in file[:location]:
                location = location - file[location::-1].index(k) # 왼쪽 가장 오른쪽에 있는거
            else:
                location = len(file) - file[::-1].index(k) -1 # 맨 오른쪽에 있는거
        if M < location:
            for l in file[:M+1]:
                if l == file[M]:
                    count += 1
            count += file[location:].count(file[M])
        else:
            for l in file[location:M+1]:
                if l == file[M]:
                    count += 1
        for i in level[:level.index(file[M])]: 
            count += file.count(i)
    print(count)
