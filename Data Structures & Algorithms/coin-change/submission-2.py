class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        change = [float("inf")] * (amount + 1)
        change[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if (i - coin) >= 0:
                    change[i] = min(change[i], change[i - coin] + 1)
        
        return change[amount] if change[amount] != float("Inf") else -1
        