class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def recurse(idx: int, curr_result: List[int], curr_sum: int):
            if curr_sum == target:
                result.append(list(curr_result))
                return
            if idx >= len(candidates) or curr_sum > target:
                return
            
            # Try adding candidates[i]
            curr_result.append(candidates[idx])
            recurse(idx + 1, curr_result, curr_sum + candidates[idx])
            curr_result.pop()
            
            # Move on to i + 1
            while idx < len(candidates) - 1 and candidates[idx+1] == candidates[idx]:
                idx += 1
            recurse(idx + 1, curr_result, curr_sum)
            
                    
        recurse(0, [], 0)
        return result