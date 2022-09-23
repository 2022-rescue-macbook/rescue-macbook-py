t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    importances = list(map(int, input().split()))
    documents = [i for i in range(n)]

    printout, res = -1, 0
    mx = max(importances)
    while printout != m: 
        front = importances.pop(0)
        document = documents.pop(0)

        if front < mx:
            importances.append(front)
            documents.append(document)
        else:
            printout = document
            res += 1
            if importances:
                mx = max(importances)
            
    print(res)
