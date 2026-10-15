class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in cache:
                return [cache[nums[i]], i]
            cache[diff] = i
        return []
