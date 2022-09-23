caseNo=int(input())
for x in range(caseNo):
    docNo, doc=map(int,input().split())
    doc_list=list(map(int,input().split()))

    idx=[i for i in range(len(doc_list))]
    result=[]
    result_idx=[]

    if len(doc_list)==1:
        print(1)
    else:
        while True:

            if doc_list[0]==max(doc_list):
                result.append(doc_list.pop(0))
                result_idx.append(idx.pop(0))
                if result_idx[-1] == doc:
                    print(len(result))
                    break
            else:
                doc_list.append(doc_list.pop(0))
                idx.append(idx.pop(0))