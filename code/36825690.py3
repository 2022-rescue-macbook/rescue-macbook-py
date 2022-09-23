num = int(input())
for i in range(num):
    document_count, location = list(map(int,input().split()))
    if document_count==1:
        document=[int(input())]
    else:
        document=list(map(int,input().split()))

    new_priorities = document # 새로운 배열 생성
    highest_priority = max(new_priorities) # 우선순위가 높은 문서 선택
    my_document = document[location] # 내가 요청한 문서
    my_index = location # 내가 속해있는 문서 위치
    cnt = 0 # 인쇄 번째를 더해줄 변수 생성
    high_index = 0  #제일 중요한 프린터 인덱스

    while highest_priority != my_document:
        # 프린터를 뽑기 위해선 항상 문서 순서를 기억해야함
        try:
            high_index = new_priorities.index(highest_priority, high_index)
        # 대기 목록에 없을 경우 다음 순서로 넘어감
        except:
            high_index = new_priorities.index(highest_priority)
        # 우선순위 위치가 내 문서 위치보다 뒤에 있으면 나의 문서 위치는 바뀌지 않는다.
        if high_index > my_index:
            new_priorities.pop(high_index)
            highest_priority = max(new_priorities)
            cnt += 1
        # 앞에 있을 경우 내 문서는 한칸 앞으로 이동
        else:
            new_priorities.pop(high_index)
            highest_priority = max(new_priorities)
            my_index -= 1
            cnt += 1

    if high_index > my_index:
        # high_index를 기준으로 양쪽으로 나눠서 my_document와 같은 값들을 비교
        high_index_list = new_priorities[high_index:]
        high_index_list = list(filter(lambda x: x == my_document, high_index_list))
        my_index_list = new_priorities[:my_index]
        my_index_list = list(filter(lambda x: x == my_document, my_index_list))
        cnt += (len(high_index_list) + len(my_index_list))
    elif high_index < my_index:
        # high_index와 my_index의 사이 값으로 계산
        result_list = new_priorities[high_index:my_index]
        result_list = list(filter(lambda x: x == my_document, result_list))
        cnt += len(result_list)
    print(cnt+1)
