class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen, max_len = set(), 0
        l, r = 0, 0
        while r < len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len