#Dynamic programming approach. O(c*a) time, O(a) space (c,a = length of coins, amount).
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1
        
        track = [0] + [float('inf')]*amount
        
        for c in range(1, amount+1):
            
            track[c] = min([track[c-coin] if c-coin>=0 else float('inf') for coin in coins])+1
            
            
        answer =  track[amount] if track[amount] != float('inf') else -1
        return answer
