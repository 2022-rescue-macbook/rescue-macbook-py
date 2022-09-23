t = int(input())
for i in range(t):
    n, m = map(int, input().split())    #n: 문서의 수 / m: 궁금한문서
    s = list(map(int, input().split())) #s: 우선순위 배열
    #여기까지 입력

    s_ = [0 for i in range(n)]  #실제 문서(큐로 쓸 것)=> 여기서는 테스트 케이스가 작아서 리스트 사용가능
    s_[m] = 1
    cnt = 0
    while True:
        if s[0] == max(s):  #가장 앞에 것이 우선순위가 가장 높다면 => 이놈을 지워야함
            cnt += 1
            if s_[0] == 1:  #이놈이 우리가 궁금한 놈이면 => 출력하고 끝내야함
                print(cnt)
                break
            else:
                del s[0]
                del s_[0]
        else:               
            s.append(s[0])
            del s[0]
            s_.append(s_[0])
            del s_[0]