import sys

'''프린터 큐
입력 : 문서 리스트, 알고싶은 문서 위치 
출력: 문서의 출력 번째수'''
def get_doc_count(doc_queue, doc_loc):
    count = 0

    while True:
        while doc_loc is not 0:
            importance = doc_queue[0]
            if len(doc_queue) is not 1 and importance < max(doc_queue[1:]):
                doc_queue.append(doc_queue.pop(0))
            else:
                doc_queue.pop(0)
                count += 1
            doc_loc -= 1

        if len(doc_queue) is not 1 and doc_queue[0] < max(doc_queue[1:]):
            doc_queue.append(doc_queue.pop(0))
            doc_loc = len(doc_queue)-1
        else:
            doc_queue.pop(0)
            count += 1
            break
    return count

if __name__ == '__main__':
    test_case_num = int(input())
    for _ in range(test_case_num):
        n, loc = list(map(int, str(sys.stdin.readline()).rstrip().split(' ')))
        queue = list(map(int, str(sys.stdin.readline()).rstrip().split(' ')))
        print(get_doc_count(queue, loc))

