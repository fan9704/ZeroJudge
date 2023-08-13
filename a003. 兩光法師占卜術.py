d = {
    0:"普通",
    1:"吉",
    2:"大吉"
}
nums = list(map(int,input().split()))

print(f'{d[(nums[0]*2+nums[1])%3]}')