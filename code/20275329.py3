testCase = int(input())
def process(D, docs):
    def putBack():
        tmp, tmpIdx = docs[0], indexTag[0]
        del docs[0]
        del indexTag[0]
        docs.append(tmp)
        indexTag.append(tmpIdx)
    
    cnt = 1
    indexTag = [i for i in range(len(docs))]
    
    while True:
#         print(docs)
        hasBigger = False
        firstVal = docs[0]
        for i in range(1, len(docs)):
            if firstVal < docs[i]:
#                 print("before",docs, indexTag)
                putBack()
#                 print("after",docs, indexTag)
                hasBigger = True
                break
            else:
                continue
        #만약 중간에 더 가치가 큰게 없으면 삭제시킴
        if not hasBigger:
            tag = indexTag[0]
            del docs[0]
            del indexTag[0]
            if tag == D:
                return cnt
            else:
                cnt += 1
            
        
for i in range(testCase):
    N, D = map(int, input().split())
    docs = list(map(int, input().split()))
    print(process(D, docs))
    
        
    