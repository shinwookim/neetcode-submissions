class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        freqs = {}
        for key, v in freq.items():
            l = freqs.get(v, list())
            l.append(key)
            freqs[v]= l

        topFreqs = sorted(list(freqs.keys()), reverse=True)
        res = []
        i, cnt = 0, 0
        while cnt < k and i < len(topFreqs):
            res += freqs[topFreqs[i]]
            cnt += len(freqs[topFreqs[i]])
            i += 1
        return res


