for _ in range(int(input())):
    arr_size, index = map(int, input().split(' '))
    q = list(map(int, input().split(' ')))
    chk = [0 for _ in range(arr_size)]
    chk[index] = 'T' #타겟 설정

    count = 0
    while True:
        if q[0] == max(q): #현재 값이 출력 대상이라면
            count += 1
            if chk[0] == 'T': #타겟이 맞는지
                print(count)
                break
            else:
                q.pop(0)
                chk.pop(0)
        else:
            q.append(q.pop(0))
            chk.append(chk.pop(0))