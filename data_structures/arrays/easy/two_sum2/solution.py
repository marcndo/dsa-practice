def two_sum(nums, target):
    l, r = 0, len(nums) - 1
    while l<r:
        result = nums[l] + nums[r]
        if result == target:
            return [l+1, r+1]
        elif result < target:
            l += 1
        else:
            r -= 1
    