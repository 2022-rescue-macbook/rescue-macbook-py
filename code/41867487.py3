import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n,m = list(map(int, input().split()))
    doc = list(map(int, input().split()))
    posDoc = list(range(len(doc)))
    posDoc[m] = "1"
    order = 0
    while doc:
        if doc[0]== max(doc):
            order += 1
            if posDoc[0]== "1":
                print(order)
                break
            else:
                doc.pop(0)
                posDoc.pop(0)
        else:
            doc.append(doc.pop(0))
            posDoc.append(posDoc.pop(0))        