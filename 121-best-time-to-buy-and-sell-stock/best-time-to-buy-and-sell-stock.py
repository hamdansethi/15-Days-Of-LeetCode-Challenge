class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        b = prices[0]
        prof = 0  

        for i in range(1, len(prices)):
            if prices[i] < b:
                b = prices[i] 
            elif prices[i] - b > prof:
                prof = prices[i] - b 

        return prof
        