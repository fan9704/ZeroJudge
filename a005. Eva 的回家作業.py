def geometric(s, nums):
    print(s+str(int((nums[1] / nums[0]) * nums[-1])))


for _ in range(int(input())):
    nums = list(map(int, input().split()))
    rate = nums[1] - nums[0]
    numsType = True

    s = ""
    for i in nums:
        s += f"{i} "

    for i in range(1, len(nums) - 1):
        if rate == nums[i + 1] - nums[i]:
            continue
        else:
            numsType = False
    if numsType:
        print(s+str(int(nums[-1] + rate)))
    else:
        geometric(s, nums)
