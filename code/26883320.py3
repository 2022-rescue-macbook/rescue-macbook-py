import sys

testCase = int(sys.stdin.readline())
for t in range(testCase):
    n,m = map(int, sys.stdin.readline().split(' '))
    nums = list(map(int, sys.stdin.readline().split(' ')))
    
    num_cnt = dict()
    for n in nums:
        num_cnt[n] = num_cnt.get(n,0)+1
        
    num_find = nums[m]
    
    max_num = 9
    cnt = 0
    while(max_num > num_find):
        if(num_cnt.get(max_num,0) == 0):
            max_num -= 1
            continue
        tmp = nums[0]
        nums.pop(0)
        m -= 1
        if(tmp == max_num ):
            num_cnt[max_num] -= 1
            cnt += 1
        else:
            nums.append(tmp)
            if(m <0 ):
                m = len(nums)-1
    for i in range(m+1):
        if( nums[i] == num_find ):
            cnt += 1
    print(cnt)
        
    
    
