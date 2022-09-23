def IntArrInput():
    return [int(v) for v in input().split(" ")]
def findBiggestIdx(arr):
    bigVal=bigIdx=0
    for (idx,val) in enumerate(arr):
        if bigVal<val:
            bigVal=val
            bigIdx=idx
    return bigIdx
def findRequireIdx(arr):
    for (i,v) in enumerate(arr):
        if v==-1: return i
def run():
    loopRange=int(input())

    for _ in range(loopRange):
        [docCnt,requireIdx]=IntArrInput()
        docArr=IntArrInput()
        docArr=docArr[:docCnt]
        cnt=0
        while True:
            biggestIdx=findBiggestIdx(docArr)
            cnt+=1
            if biggestIdx==requireIdx:
                print(cnt)
                break
            else:
                requireIdxNum=docArr[requireIdx]
                docArr[requireIdx]=-1
                docArr=docArr[biggestIdx+1:]+docArr[:biggestIdx]
                requireIdx=findRequireIdx(docArr)
                docArr[requireIdx]=requireIdxNum
run()