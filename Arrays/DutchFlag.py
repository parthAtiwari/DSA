def dutch_flag(nums):
    def partition(i):
        pivot = nums[i]
        smaller = 0
        for ix in range(len(nums)):
            if nums[ix] < pivot:
                nums[ix], nums[smaller] = nums[smaller], nums[ix]
                smaller += 1

        larger = len(nums)-1
        for jx in reversed(range(len(nums))):
            if nums[jx] < pivot:
                break
            elif nums[jx] > pivot:
                nums[larger], nums[jx] = nums[jx], nums[larger]
                larger -= 1
    for i in range(len(nums)):
        partition(i)


def dutch_flagV2(nums):
    def partition(i):

        pivot = nums[i]
        smaller, equal, larger = 0, 0, len(nums)
        while equal < larger:

            if nums[equal] < pivot:

                nums[smaller], nums[equal] = nums[equal], nums[smaller]
                equal += 1
                smaller += 1
            elif nums[equal] == pivot:
                equal += 1
            else:
                
                larger -= 1
                nums[equal], nums[larger] = nums[larger], nums[equal]
    for i in range(len(nums)):
        partition(i)
    
