from sys import stdin

tc = int(input())
result = list()

for i in range(tc):
    n, m = list(map(int, stdin.readline().split()))
    doc = list(map(int, stdin.readline().split()))
    cursor = [0] * n
    cursor[m] = 1
    cnt = 0
    
    while True:
        if doc[0] == max(doc):
            cnt += 1
            if cursor[0] == 1:
                result.append(cnt)
                break
            else:
                del doc[0]
                del cursor[0]
        else:
            doc.append(doc[0])
            del doc[0]
            cursor.append(cursor[0])
            del cursor[0]

for i in result:
    print(i)