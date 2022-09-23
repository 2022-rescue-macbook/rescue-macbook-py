import sys
input = sys.stdin.readline
arr = []
A = int(input())
for i in range(A):
    B, C = map(int, input().split())
    imp = list(map(int, input().split()))
    T = []
    arr2 = []
    for i in range(B):
        T.append(i+1)
    while imp :
        for i in imp:
            if max(imp)>imp[0]:
                imp.append(imp[0])
                T.append(T[0])
                imp.remove(imp[0])
                T.remove(T[0])
            else :
                arr.append(imp[0])
                arr2.append(T[0])
                imp.remove(imp[0])
                T.remove(T[0])
    print(arr2.index(C+1)+1)
