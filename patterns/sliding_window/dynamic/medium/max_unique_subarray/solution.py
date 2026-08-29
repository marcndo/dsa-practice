def max_unique_subarray(nums):
    l = 0
    max_sum = 0
    window_sum = 0
    seen = set()
    for r in range(len(nums)):
        while nums[r] in seen:
            window_sum -= nums[l]
            seen.remove(nums[l])
            l += 1
        seen.add(nums[r])
        print(seen)
        window_sum += nums[r]
        max_sum = max(max_sum, window_sum)
    return max_sum