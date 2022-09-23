test_num = int(input())
results = []

for test in range(test_num):
    n, m = list(map(int, input().split(" ")))
    cnt = 1
    important_docs = list(map(int, input().split(" ")))[:n]

    for idx in range(n):
        max_idx = important_docs.index(max(important_docs))
        pre = important_docs[:max_idx]
        post = important_docs[max_idx + 1:]
        
        if max_idx == m:
            results.append(f"{cnt}")
            break
        elif m < max_idx:
            m = len(post) + m
        elif m > max_idx:
            m -= (max_idx + 1)

        post.extend(pre)
        important_docs = post
        cnt += 1

print("\n".join(results))