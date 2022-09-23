import sys
input = sys.stdin.readline

for _ in range(int(input())):
    M ,S =map(int,input().split())
    data = list(map(int,input().split()))
    comp = sorted(data)
    data = [(idx,T) for idx,T in enumerate(data)]
    cnt = 1
    while data:        
        if data[0][1]<comp[-1]:
            data.append(data.pop(0))
        else:
            if data[0][0] == S:
                print(cnt)
                break
            else:
                data.pop(0)
                comp.pop()
                cnt+=1
