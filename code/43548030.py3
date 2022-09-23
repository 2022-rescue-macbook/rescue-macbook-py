from sys import stdin
n = int(stdin.readline())
result = []
for _ in range(n):
    # N : 문서의 개수, M : 몇 번째로 인쇄되었는지 궁금한 문서 인덱스
    N, M = map(int, stdin.readline().split())
    # data : N개의 문서의 중요도 리스트
    data = list(map(int, stdin.readline().split()))
    
    out = 0
    t = M
    
    while(True):
        # 9 1 '1' 1 9 9     out=0 t=2
        # 1 '1' 1 9 9       out=1 t=1
        # '1' 1 9 9 1             t=0
        # 1 9 9 1 '1'             t=len(list)-1=4
        # 9 9 1 '1' 1             t=3
        # 9 1 '1' 1         out=2 t=2
        # 1 '1' 1           out=3 t=1
        # '1' 1             out=4 t=0
        # '1' 출력          out=5 
        # print(out, t)
        if data[0] == max(data):
            out+=1
            if t==0:
                result.append(out)
                break;
            else:
                t-=1
                del data[0]
        else:
            if t==0:
                data.append(data[0])
                del data[0]
                t=len(data)-1
            else:
                data.append(data[0])
                del data[0]
                t-=1

for i in result:
    print(i)
