class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        profit1, profit2 = [0] * (n + 2), [0] * (n + 2)

        # Skip house 0
        for i in range(n - 1, 0, -1):
            profit1[i] = max(nums[i] + profit1[i + 2], profit1[i + 1])

        # Rob house 0 (so, skip house 1 and last house)
        for i in range(n - 2, 1, -1):
            profit2[i] = max(nums[i] + profit2[i + 2], profit2[i + 1])

        return max(profit1[1], profit2[2] + nums[0])
        