class Solution:
    """
    @param prices: a list of integers
    @param fee: a integer
    @return: return a integer
    """
    def maxProfit(self, prices, fee):
        unhold, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            unhold, hold = max(unhold, hold + prices[i] - fee), max(hold, unhold - prices[i])
        return unhold



'''
https://www.jiuzhang.com/solution/best-time-to-buy-and-sell-stock-with-transaction-fee/#tag-highlight-lang-python
'''

'''

if (prices == null || prices.length == 0) {
            return 0;
        }
        int[] hold = new int[prices.length]; // hold[i] - the max profit we get if we keep the stock at ith day
        int[] unhold = new int[prices.length]; // unhold[i] - the max profic we get if we dont have stock at ith day
        hold[0] = -prices[0];
        unhold[0] = 0;
        for (int i = 1; i < prices.length; i++) {
            hold[i] = Math.max(hold[i - 1], unhold[i - 1] - prices[i]);
            unhold[i] = Math.max(unhold[i - 1], hold[i - 1] + prices[i] - fee);
        }
        return unhold[prices.length - 1];

        
'''