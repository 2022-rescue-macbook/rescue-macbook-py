import sys

t = int(sys.stdin.readline())
for i in range(t):
    page_count, cur_page = map(int,sys.stdin.readline().split())
    importance = list(map(int,sys.stdin.readline().split()))
    pages = list(range(page_count))
    cnt = 1
    while True:
        if importance[0] == max(importance):
            if pages[0] == cur_page:
                print(cnt)
                break
            else:
                pages.pop(0)
                importance.pop(0)
                cnt += 1
        back = pages[:importance.index(max(importance))]
        pages = pages[importance.index(max(importance)):] + back
        back = importance[:importance.index(max(importance))]
        importance = importance[importance.index(max(importance)):] + back