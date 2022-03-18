n, m, k = 5, 8, 3
nums = [2, 4, 5, 4, 6]

def bigNum(n, m, k, nums):
    answer = 0
    nums = sorted(nums, reverse=True)
    if nums[0] == nums[1]:
        answer += nums[0] * k
    else: 
        while m > 0:
            if m < (k + 1):
                answer += nums[0] * m
                break
            else:
                answer += nums[0] * k
                answer += nums[1]
                m -= (k + 1)
    return answer

print(bigNum(n, m, k, nums))