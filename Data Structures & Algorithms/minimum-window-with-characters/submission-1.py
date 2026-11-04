from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        freq_s = dict()
        freq_t = dict(Counter(t))
        l, r = 0, 0
        min_len, min_str = len(s) + 1, ""
        while r < len(s):
            freq_s[s[r]] = freq_s[s[r]] + 1 if s[r] in freq_s else 1
            
            
            while (s[l] not in freq_t or freq_s[s[l]] > freq_t[s[l]] )and l < r:
                freq_s[s[l]] -= 1
                l += 1

            if all(freq_s.get(c, 0) >= count for c, count in freq_t.items()) and (r - l + 1) < min_len:
                min_len, min_str = (r - l + 1), s[l:r+1]
            r += 1
        return min_str
