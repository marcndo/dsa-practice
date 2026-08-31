#method one
def min_value(nums):
    min_val = nums[-1]
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r) // 2
        if nums[m] < min_val:
            min_val = nums[m]
            r = m - 1
        else:
            l = m + 1
    return min_val


def find_min(nums):
    left = 0 
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid 
    return nums[left]

