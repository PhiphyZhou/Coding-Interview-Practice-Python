# 122. Best Time to Buy and Sell Stock II (Bloomberg)
# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        have_stock = False
        buy = -1
        total = 0
        
        for i in range(len(prices)):
            if not have_stock:
                if i<len(prices)-1 and prices[i]<prices[i+1]:
                    buy = i
                    have_stock = True
            else:
                if i==len(prices)-1 or prices[i]>prices[i+1]:
                    total += prices[i] - prices[buy]
                    have_stock = False
        return total
        
# Note: if you don't care about the strategy, just the profite, you can simply sum up all 
# the differences that p[i+1]>p[i]: 
# for (int i=0; i< prices.length-1; i++) {
#         if (prices[i+1]>prices[i]) total += prices[i+1]-prices[i];
#     }