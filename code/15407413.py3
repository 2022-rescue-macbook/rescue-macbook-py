def solution(N, M, nums):
    count_dict = {}
    for numtup in nums:
        if not numtup[1] in count_dict.keys():
            count_dict.update({numtup[1]:0})
        count_dict.update({numtup[1]: count_dict.get(numtup[1]) + 1})
    dict_keys = list(count_dict.keys())
    dict_keys.sort(reverse=True)
    dict_q = []
    for dict_key in dict_keys:
        for i in range(count_dict.get(dict_key)):
            dict_q.append(dict_key)

    answer = 0
    cur_priority = dict_q.pop(0)
    while True:
        if nums[0][1] != cur_priority:
            nums.append(nums[0])
            nums.pop(0)
            # print('set back', nums)
        else:
            if nums[0][0]==M:
                answer += 1
                # print('answer', nums)
                break
            else:
                nums.pop(0)
                answer += 1
                cur_priority = dict_q.pop(0)
                # print('prioriy pop', nums)
                # print('cur priority', cur_priority)
    # print(answer)
    return answer

if __name__ == '__main__':
    count_cases = int(input())
    for i in range(count_cases):
        N, M = [int(x) for x in input().split(' ')]
        nums = [(i, int(x)) for i, x in enumerate(input().split(' '))]
        answer = solution(N, M, nums)
        print(answer)
