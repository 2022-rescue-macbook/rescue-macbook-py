import sys

t = int(input())
for _ in range(t):
    pages, what_page = map(int, input().split())
    priority = list(map(int, sys.stdin.readline().split()))
    page_list = [i for i in range(pages)]
    page_list[what_page] = 'target'
    cnt = 0
    while True:
        if priority[0] == max(priority):
            cnt += 1
            if page_list[0] == 'target':
                print(cnt)
                break
            else:
                priority.pop(0)
                page_list.pop(0)
        else:
            priority.append(priority.pop(0))
            page_list.append(page_list.pop(0))
