from sys import stdin

def solution(M, imp):
    count = 0
    top = max(imp, key = lambda x:x[1])
    
    while(imp):
        item = imp.pop(0)
        if item[1] == top[1]:
            count += 1
            if item[0] == M:
                return count
            else:
                top = max(imp, key = lambda x:x[1])
        else:
            imp.append(item)
            
for _ in range(int(stdin.readline())):
    N, M = map(int, stdin.readline().split())
    imp = list(enumerate(map(int, stdin.readline().split())))
    
    print(solution(M, imp))