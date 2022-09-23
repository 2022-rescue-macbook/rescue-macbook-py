TN = int(input()) # 테스트 케이스의 수
for test_case in range(TN):
    #print("test case #{0}".format(test_case))
    N,M = map(int,input().split())
    counter = 0 # counter for print turn
    pos = M # position of M
    docs = list(map(int,input().split()))
    mx = max(docs)
    while True:
        #print("{0}을 처리 중입니다.".format(docs[0]))
        if docs[0] == mx:
            #print('{0}가 최대값입니다.프린트합니다'.format(docs[0]))
            #print(docs)
            counter += 1
            del docs[0]
            if pos == 0:
                print(counter)
                break
            else:
                pos -= 1
            mx = max(docs)
        else:
            docs.append(docs[0])
            del docs[0]
            if pos == 0:
                pos =len(docs) - 1
            else:
                pos -= 1