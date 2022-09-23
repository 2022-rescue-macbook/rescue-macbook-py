# 프린터 큐
n = int(input())
result=[]
for i in range(n):
    a,b = map(int, input().split())# a는 문서의 개수, b는 출력 순번을 알고자하는 문서의 위치
    x= input().split()
    y=[]
    #y는 처음 입력받은 문서의 중요도 리스트
    for j in range(a):
        y.append(x[j])
    x.sort(reverse=True) #x는 문서의 중요도 리스트를 내림차순 시킨 것
    position=0 #y를 원형큐로 사용하기 위해 현재 위치를 나타내는 변수

    for j in range(a):# 문서의 개수만큼 반복
        while 1:
            if y[position] == x[j]: #만약 찾고있는 중요도가 리스트(y)에서 발견되었는데
                if position==b: #y에서 발견된 위치와 출력 순번을 알고자하는 문서의 위치가 동일하다면
                    result.append(j+1) # j+1번째에 출력되었습니다. (결과리스트에 추가)
                # 포지션 증가 (원형큐)
                if position == a - 1:
                    position = 0
                else:
                    position += 1
                break
            # 포지션 증가 (원형큐)
            if position == a-1:
                position=0
            else:
                position +=1

for i in range(n):
    print(result[i])