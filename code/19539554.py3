t = int(input()) #tast case

for i in range(t):
    n,m =map(int, input().split())
    notes = list(map(int, input().split()))
    count = 0
    idx = m
    while True:
        if notes[0] == max(notes):
            count +=1
            if idx==0:
                print(count)
                break
            else:
                if idx>0:
                    idx-=1
                notes.pop(0)
        else:
            if idx>0:
                idx-=1
            else:
                idx=len(notes)-1
            notes.append(notes.pop(0))
