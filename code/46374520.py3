import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    docs = list(map(int, input().split()))
    idx = list(range(len(docs)))
    idx[m] = 'answer'
    
    order = 0
    
    while True:
        if docs[0] == max(docs):
            order += 1

            if idx[0] == 'answer':
                print(order)
                break
            else:
                docs.pop(0)
                idx.pop(0)
        
        else:
            docs.append(docs.pop(0))
            idx.append(idx.pop(0))