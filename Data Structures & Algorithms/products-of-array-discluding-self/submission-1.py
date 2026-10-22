# In: [1,2,4,6]
# Out: [2 * 4 * 6, 1 * 4 * 6, 1 * 2 * 6, 1 * 2 * 4]
# So Out[i] = Prefix[i] * Suffix[i]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1] * len(nums), [1] * len(nums)
        for i in range(len(nums)):
            if i < len(nums) - 1:
                prefix[i + 1] = prefix[i] * nums[i]
        for i in range(len(nums)-1,0,-1):
            if i > 0:
                suffix[i - 1] = suffix[i] * nums[i]
     
        soln = [0] * len(nums)
        for i in range(len(nums)):
            soln[i] = prefix[i] * suffix[i]

        return soln