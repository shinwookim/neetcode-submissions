class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def recursive_sum(i: int, curr_result: List[int], curr_sum: int):
            if curr_sum == target:
                result.append(list(curr_result))
                return
            if i >= len(nums) or curr_sum > target:
                return
            
            # Try adding nums[i]
            curr_result.append(nums[i])
            recursive_sum(i, curr_result, curr_sum + nums[i])
            curr_result.pop()
            
            # Move on to i + 1
            recursive_sum(i + 1, curr_result, curr_sum)
            
                    
        recursive_sum(0, [], 0)
        return result