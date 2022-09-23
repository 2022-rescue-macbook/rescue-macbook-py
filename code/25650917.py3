def pop_and_push(arr):
    tmp=arr.pop(0)
    arr.append(tmp)

val_case=int(input())
for i in range(val_case):
    val_size,val_idx=map(int,input().split())
    db_score=list(map(int,input().split()))
    
    db_idx=list(range(val_size))
    sv_idx=db_score[val_idx]
    sv_max=max(db_score)
    cnt=1

    while sv_max>sv_idx:
        while db_score[0]!=sv_max:
            pop_and_push(db_score)
            pop_and_push(db_idx)
        db_score.pop(0)
        db_idx.pop(0)
        cnt+=1
        sv_max=max(db_score)
    for i in range(len(db_score)):
        if db_idx[i]!=val_idx:
            if db_score[i]==sv_idx:cnt+=1
        else:break
    print(cnt)