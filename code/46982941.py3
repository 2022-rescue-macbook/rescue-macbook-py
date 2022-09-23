import sys

input =sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    A = list(map(int, input().rstrip().split()))
    idx = list(range(n)) 
    result = 0
    while True:
        if A[0]==max(A):
            result+=1
            if idx[0]==m:
                print(result)
                break
            else:
                A.pop(0)
                idx.pop(0)
        else:
            A.append(A.pop(0))
            idx.append(idx.pop(0))