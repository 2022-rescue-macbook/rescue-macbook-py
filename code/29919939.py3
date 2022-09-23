# 문제수
testCnt = int(input())
ans = []

for i in range(testCnt):
    # 문서수, 알고싶은 문서번호
    printCnt, printNum = map(int, input().split())

    # 프린트큐
    printQue = list(map(int, input().split()))

    # 문서출력 카운트
    cnt = 0

    while printQue:
        # 출력여부
        isPrint = True

        for j in range(1, len(printQue)):
            # 현재문서보다 큰 문서가 있으면 출력안함
            if printQue[0] < printQue[j]:
                isPrint = False
                break

        if isPrint:
            # 출력수 카운트
            cnt += 1

            # 출력
            printQue.pop(0)

            # 현재문서가 내가 알고싶은 문서이면 종료
            if printNum == 0:
                ans.append(cnt)
                break
        else:
            # 출력을 하지 않고 현재문서를 가장 뒤로
            printQue.append(printQue.pop(0))

        if printNum == 0:
            printNum = len(printQue) - 1
        else:
            printNum -= 1

for i in ans:
    print(i)