class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
        
            curr = res.get(tuple(freq), [])
            curr.append(s)
            res[tuple(freq)] = curr
        
        return list(res.values())
            
