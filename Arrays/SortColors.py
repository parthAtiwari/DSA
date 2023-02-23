# Leetcode 75
class Solution:
    def sort_colors(self, nums: List[int]) -> None:
        def solve(i):
            pivot = nums[i]
            smaller = 0
            for i in range(len(nums)):
                if nums[i] < pivot:
                    nums[i], nums[smaller] = nums[smaller], nums[i]
                    smaller += 1
            larger = len(nums)-1
            for i in reversed(range(len(nums))):
                if nums[i] < pivot:
                    break
                elif nums[i] > pivot:
                    nums[i], nums[larger] = nums[larger], nums[i]
                    larger -= 1

        for i in range(len(nums)):

            solve(i)