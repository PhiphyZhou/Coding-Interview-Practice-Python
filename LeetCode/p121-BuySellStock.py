# 121. Best Time to Buy and Sell Stock (Amazon Microsoft Bloomberg Uber Facebook)
# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = -1
        sell = -1
        cand = 0 # the possible new buy
        
        for i in range(1,len(prices)):
            if prices[i]<prices[cand]: cand = i
            elif (prices[i]-prices[cand]>prices[sell]-prices[buy] or 
                    (prices[i]>prices[cand] and sell == -1)):
                sell = i
                buy = cand
            print i, cand, buy, sell
        
        if sell == -1:
            prof = 0
        else:
            prof = prices[sell] - prices[buy]
        
        return prof