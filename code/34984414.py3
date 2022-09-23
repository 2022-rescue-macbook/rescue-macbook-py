t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    doc = list(map(int, input().split()))
    sorted_doc = sorted(doc, reverse=True)
    pointer = 0
    cnt = 1
    while True:
        if doc[pointer] != sorted_doc[0]:
            pointer += 1
            pointer %= len(doc)
            continue
        if pointer == m:
            print(cnt)
            break
        del doc[pointer]
        del sorted_doc[0]
        if pointer < m:
            m -= 1
        pointer %= len(doc)
        cnt += 1