from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        freq_s = dict()
        freq_t = dict(Counter(t))

        satisfied, required = 0, len(freq_t)
        min_len, min_str = len(s) + 1, ""

        l, r = 0, 0
        while r < len(s):
            freq_s[s[r]] = freq_s[s[r]] + 1 if s[r] in freq_s else 1
            
            if s[r] in freq_t and freq_s[s[r]] == freq_t[s[r]]:
                satisfied += 1

            while satisfied == required:
                if (r - l + 1) < min_len:
                    min_len, min_str = (r - l + 1), s[l:r+1]

                freq_s[s[l]] -= 1
                if s[l] in freq_t and freq_s[s[l]] < freq_t[s[l]]:
                    satisfied -= 1
                l += 1
            r += 1
        return min_str
