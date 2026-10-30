class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        seen = set()
        l, r = 0, 0
        while(r < len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                best = max(best, (r - l + 1))
                r += 1
            else:
                while l < r:
                    seen.remove(s[l])
                    l += 1
                    if s[l - 1] == s[r]:
                        break
        return best
