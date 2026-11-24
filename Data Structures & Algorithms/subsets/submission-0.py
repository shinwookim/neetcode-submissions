class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, subset = [], []
        def buildSubset(idx):
            if idx == len(nums):
                ans.append(subset.copy())
                return
            subset.append(nums[idx])
            buildSubset(idx + 1)
            subset.pop()
            buildSubset(idx + 1)
        buildSubset(0)
        return ans
            
