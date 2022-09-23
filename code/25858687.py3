testCase = int(input())

for _ in range(testCase):
    docuNum, findIndex = list(map(int, input().split()))
    documents = list(map(int, input().split())) # 큐 ㅋ_ㅋ
    outputNum = 1
    find = 0

    while docuNum > 0:                      # 큐에 값이 들어 있을 때
        popNum = documents.pop(0)           # 첫 번째 수 빼놓음
        for i in range(docuNum - 1):            # 문서 큐 돌림
            if popNum < documents[i]:       # 더 큰게 있으면
                findIndex = (findIndex - 1 + docuNum) % docuNum
                documents.append(popNum)    # 뒤로 돌려놈
                break
        else:                               # 더 큰게 없었는데
            if findIndex == 0:
                print(outputNum)
                break
            else:
                docuNum -= 1
                findIndex = (findIndex - 1 + docuNum) % docuNum
                outputNum += 1