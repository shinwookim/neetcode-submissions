class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def _mostCommonChar(freqs: dict) -> str:
            c, m = "", 0
            for k, v in freqs.items():
                if v > m:
                    c, m = k, v
            return c

        freq = dict()
        l, r, max_len = 0, 0, 0

        while r < len(s):
        
            freq[s[r]] = freq.get(s[r], 0) + 1
            
            if (r - l + 1) - freq[_mostCommonChar(freq)] <= k:
                max_len = max(max_len, (r - l + 1))
            else:
                while l < r and (r - l + 1) - freq[_mostCommonChar(freq)] > k:
                    freq[s[l]] -= 1
                    l += 1
            r += 1

        return max_len