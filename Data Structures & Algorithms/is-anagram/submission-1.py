class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams must be of same length
        if len(s) != len(t):
            return False
        s_count = {}
        for s1 in s:
            if s1 in s_count:
                s_count[s1] += 1
            else:
                s_count[s1] = 1
        
        for s2 in t:
            if s2 in s_count:
                s_count[s2] -= 1
            else:
                return False

        for v in s_count.values():
            if v != 0:
                return False
            
        return True



