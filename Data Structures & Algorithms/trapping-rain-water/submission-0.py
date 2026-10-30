class Solution:
    def trap(self, height: List[int]) -> int:
        # l_maxi] := max height left of i (including i) 
        # r_max[i] := max height right of i (including i) 
        l_max, r_max = [0] * len(height), [0] * len(height)
        
        l_max [0]= height[0]
        for l in range(1, len(height)):
            l_max[l] = max(l_max[l - 1], height[l])
        
        r_max[len(height) - 1] = height[len(height) - 1]
        for r in range(len(height) - 2, -1, -1):
            r_max[r] = max(r_max[r + 1], height[r])
        
        cumm_sum = 0
        for i in range(len(height)):
            cumm_sum += min(l_max[i], r_max[i]) - height[i]
        return cumm_sum

