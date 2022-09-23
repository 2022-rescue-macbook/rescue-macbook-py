import sys
case = int(sys.stdin.readline().rstrip('\n'))
for i in range(case):
    docnum, tgt = sys.stdin.readline().rstrip('\n').split()
    docnum, tgt = int(docnum), int(tgt)
    prior = list(map(int,sys.stdin.readline().rstrip('\n').split()))
    tgtprior = prior[tgt]
    count = 0
    while True:
        if max(prior) == prior[0]: #우선순위 최대문서가 큐의 제일 앞에 있음
            if tgt == 0: #그 문서가 타겟인 경우
                count+=1
                break
            else:
                prior.pop(0) #아닌 경우
                count +=1
                tgt -= 1
        else: #우선순위 최대 문서가 중간에 있는 경우
            if tgt ==0: #지금 큐 제일 앞이 타겟인 경우에는
                prior.append(prior.pop(0)) #앞에서 빼서 뒤에다 추가
                tgt = len(prior)-1
            else :
                prior.append(prior.pop(0))
                tgt -=1
    print(count)