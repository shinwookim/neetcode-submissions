class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def buildPermutation(p, candidates):
            if len(candidates) == 0:
                ans.append(p)
            for i in range(len(candidates)):
                buildPermutation(p +[candidates[i]], candidates[:i] + candidates[i+1:])
        buildPermutation([], nums)
        return ans