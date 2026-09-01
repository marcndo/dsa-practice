def two_sum(nums,target):
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return seen[complement], i
        else:
            seen[nums[i]] = i
