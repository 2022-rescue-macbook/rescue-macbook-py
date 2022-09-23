import sys
# 숫자 하나 입력
# num = int(sys.stdin.readline())

# 문자 하나 입력
# input = sys.stdin.readline()

# 숫자열 입력
# input = list(map(int,sys.stdin.readline().split()))

testCount = int(sys.stdin.readline())

class doc:
    def __init__(self,score, isTarget):
        self.score =score
        self.isTarget = isTarget



ret = []
for _ in range(testCount):
    docCnt, checkIdx = map(int,sys.stdin.readline().split())
    docscores = list(map(int,sys.stdin.readline().split()))
    docDatas = [doc(docscores[idx],idx == checkIdx) for idx in range(len(docscores))]

    ordval = 0
    while True:
        curDoc = docDatas.pop(0)
        bestScore = True
        for d in docDatas:
            if curDoc.score < d.score:
                docDatas.append(curDoc)
                bestScore = False
                break
        if bestScore:
            ordval += 1
            if curDoc.isTarget:
                ret.append(ordval)
                break

[print(n) for n in ret]


