#조사할 횟수 설정
test_case=int(input())
#초기값 지정. 문서수 n, 확인할 인덱스m, 우선순위 배열imp,우선순위의 인덱스 idx
for _ in range(test_case):
    n,m=list(map(int,input().split()))
    imp=list(map(int,input().split()))
    idx=list(range(len(imp)))
    idx[m]='target'
    
    #순서 값
    order=0
    while True:
        #1.우선순위 높을때
        if imp[0]==max(imp):
            order+=1#순서증가
            #2.타겟일 때
            if idx[0]=='target':
                #출력 후 리턴
                print(order)
                break
            else:#타겟은 아닐때
                imp.pop(0)
                idx.pop(0)
        else:#우선순위도 낮고 타겟도 아닐때
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))
    
    
    
    