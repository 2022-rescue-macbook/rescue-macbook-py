T = int(input())

for i in range(T):
    cnt = 0
    num, b = map(int, input().split())
    waiting = list(map(int, input().split()))
    to_find = waiting[b]
    key = [0 for _ in range(num)]
    key[b] = 'KEY'
    while True:
        if waiting[0] == max(waiting):
            cnt +=1
            if key[0] == 'KEY':
                print(cnt)
                break
            else:
                waiting.pop(0)
                key.pop(0)
        else:
            waiting.append(waiting.pop(0))
            key.append(key.pop(0))
