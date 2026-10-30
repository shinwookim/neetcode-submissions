class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, target, lo, hi) -> int:
            if lo > hi:
                return -1

            mid = lo + (hi - lo) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(nums, target, mid + 1, hi)
            else:
                return binary_search(nums, target, lo, mid - 1)
        return binary_search(nums,target, 0, len(nums)-1)