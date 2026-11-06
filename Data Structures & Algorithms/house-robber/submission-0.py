class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        DP = [0] * len(nums)
        DP[0] = nums[0]
        DP[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            DP[i] = max(nums[i] + DP[i - 2], DP[i - 1])
    
        return DP[len(nums) - 1]
        
        
        
        
        def dfs(i):
            if i >= len(nums):
                return 0
            return max(nums[i] + dfs(i + 2), dfs(i + 1))
        return dfs(0)