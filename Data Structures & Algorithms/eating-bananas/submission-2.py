class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        min_k = max(piles)
        while lo <= hi:
            k = (hi + lo) // 2
            time_required = 0
            for pile in piles:
                time_required += math.ceil(float(pile) / k)
            if time_required <= h:
                min_k = k
                hi = k - 1
            else:
                lo = k + 1
        return min_k