start=int(input())
for i in range(start):
    File=input().split()
    File_sheets=int(File[0])
    File_target=int(File[1])
    Q=input().split()
    target = [0 for i in range(File_sheets)]
    target[File_target] = 'T'
    size=0
    while size<=File_sheets:
        if Q[0]==max(Q):
            Q.pop(0)
            result=target.pop(0)
            size+=1
            if result=='T':
                print(size)
                break
        else:
            Q.append(Q.pop(0))
            target.append(target.pop(0))