test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    #enumerate : 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환
    queue_idx = [(i, idx) for idx, i in enumerate(queue)]
    count = 0
    while True:
        if queue_idx[0][0] == max(queue):
            count += 1
            if queue_idx[0][1] == m:
                print(count)
                break
            else:
                queue_idx.pop(0)
                queue.pop(0)
        else:
            queue_idx.append(queue_idx.pop(0))
            queue.append(queue.pop(0))