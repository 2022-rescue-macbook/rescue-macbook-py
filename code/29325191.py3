a = int(input())
for i in range(a):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    idx = lst.index(max(lst))
    lst[idx] = -1
    answer = 1
    leng = len(lst)
    
    while m != idx:
        try:
            idx = (idx + 1 + lst[(idx + 1) % leng:].index(max(lst))) % leng
        except:
            idx = lst[:idx].index(max(lst))
        lst[idx] = -1
        answer += 1
    print(answer)