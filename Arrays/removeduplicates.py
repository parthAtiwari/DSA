# Leetcode 26
# nums is sorted in ascending order
def remove_duplicates(nums):
    vacant = 1
    for i in range(1, len(nums)):
        if nums[vacant - 1] != nums[i]:
            nums[vacant] = nums[i]
            vacant += 1
    return vacant
