def removeDuplicates(nums):
    vacant = 1
    for i in range(1, len(nums)):
        if nums[vacant-1]!=nums[i]:
            nums[vacant] = nums[i]
            vacant += 1
    return vacant
