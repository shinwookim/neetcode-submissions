class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            srt = "".join(sorted(s))
            l = d.get(srt, list())
            l.append(s)
            d[srt] = l
        return list(d.values())
        