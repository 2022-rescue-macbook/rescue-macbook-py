testCase = int(input())

for i in range(testCase):
    cnt = 0
    n,m = map(int, input().split()) #n은 프린트할 개수 m은 주목할 인덱스
    printlsit = list(map(int, input().split()))
    s_ = [0 for i in range(n)]
    s_[m] = 1

    cnt = 0
    while 1:
        if printlsit[0] == max(printlsit):
            cnt += 1
            if s_[0] == 1:
                print(cnt)
                break
                
            else:
                del printlsit[0]
                del s_[0]
        else:
            printlsit.append(printlsit[0])
            del printlsit[0]
            s_.append(s_[0])
            del s_[0]