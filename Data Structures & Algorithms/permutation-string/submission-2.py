from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = dict(Counter(s1))
        s2_count = {}
        l, r = 0, 0
        while r < len(s2):
            if s2[r] in s1:
                s2_count[s2[r]] = s2_count[s2[r]] + 1 if s2[r] in s2_count else 1  
                if s2_count[s2[r]] == s1_count[s2[r]]: 
                    if s1_count == s2_count:
                        return True
                elif s2_count[s2[r]] > s1_count[s2[r]]:
                    while s2_count[s2[r]] > s1_count[s2[r]]:
                        s2_count[s2[l]] -= 1
                        l += 1
            else:
                s2_count = {}
                l = r + 1
            r += 1
        return False