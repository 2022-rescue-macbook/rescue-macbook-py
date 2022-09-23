import sys
import math
for i in range(0, int(input())):
    count=0
    n,m = map(int, sys.stdin.readline().split())
    papers = list(map(int,sys.stdin.readline().split()))
    mres=m
    while papers:
        if max(papers)!=papers[0]:
            papers.append(papers[0])
            del papers[0]
            if mres==0:
                mres=len(papers)-1
            else:
                mres-=1
        else:
            count+=1
            del papers[0]
            if 0==mres:
                print(count)
                break;
            mres-=1