class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < nums[hi]: # Right side is sorted
                if nums[mid] < target and target <= nums[hi]:
                    lo = mid + 1
                else: # target > nums[mid] or target >= nums[hi]
                    hi = mid - 1
            else: # nums[mid] >= nums[hi] -> Left is sorted
                if nums[lo] <= target and target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = lo + 1

        return -1