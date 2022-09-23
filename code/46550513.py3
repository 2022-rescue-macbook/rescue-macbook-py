import sys
input = sys.stdin.readline
print = sys.stdout.write

lst = []
for _ in range(int(input())) :
    N, M = map(int,input().split())
    L = list(map(int,input().split()))
    for i in range(N) :
        while M != 0 or max(L) != L[M] :
            if L[0] == max(L) :
                lst.append(L.pop(0))
            else :
                L.append(L.pop(0))
            if M == 0 : 
                M = len(L) - 1
            else :
                M -= 1
        if M == 0 and max(L) == L[M] :
            lst.append(L.pop(0))
            break
    print(f'{len(lst)}\n')
    lst = []