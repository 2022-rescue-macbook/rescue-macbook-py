import sys

input = sys.stdin.readline

test_num = int(input().rstrip())

for _ in range(test_num):
    cnt = 0
    doc_num, ans = map(int,input().split())
    priority = list(map(int,input().split()))
    qu = list(range(len(priority)))
    qu[ans] = 100

    while 1:
        if priority[0] == max(priority):
            cnt += 1
            if qu[0] == 100:
                print(cnt)
                break
            else:
                priority.pop(0)
                qu.pop(0)
        else:
            qu.append(qu.pop(0))
            priority.append(priority.pop(0))