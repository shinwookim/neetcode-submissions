class Solution:
    def climbStairs(self, n: int) -> int:
        climbStairs = [1] * (n + 1)

        for n in range(2, n + 1):
            climbStairs[n] = climbStairs[n - 2] + climbStairs[n - 1]

        return climbStairs[n]
