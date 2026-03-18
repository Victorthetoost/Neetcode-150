class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        biggest = 0
        for i in range (0,len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]-prices[i] > biggest:
                    biggest = prices[j]-prices[i]
        return biggest