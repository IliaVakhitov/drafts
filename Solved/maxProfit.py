# Best Time to Buy and Sell Stock II

from typing import List

class Solution(object):
    # TODO Solve with matrix profits
    #
    def run(self):
        print(str(self.maxProfit([7,1,5,3,6,4])) + ' expected 7')
        print(str(self.maxProfit([1,2,3,4,5])) + ' expected 4')
        print(str(self.maxProfit([7,6,4,3,1])) + ' expected 0')
        prices = [7,1,5,3,6,4,11,4,5,6,
            3,4,7,8,10,88,776,4,4,5,
            66,553,22,1,1111,3,4,5,
            6,7,8,6,5,5,5,5,5,33,4,
            444,6,78,8,89
        ]
        print(f'{self.maxProfitLinear(prices)} expected 3074')
        
        prices = [7,1,5,3,6,4,8,4,5,6,3,4,7,8,9,8,6,4,4,5,6,5,2,1,1,3,4,5,6,7,8,6,5,5,5,5,5,3,4,4,6,8,8,9]
        print(f'{self.maxProfitLinear(prices)} expected 34')


    def maxProfitLinear(self, prices: List[int]) -> int:
        """
        In this case, instead of looking for every peak following a valley, 
        we can simply go on crawling over the slope and keep on adding the profit 
        obtained from every consecutive transaction. 
        In the end,we will be using the peaks and valleys effectively, 
        but we need not track the costs corresponding to the peaks 
        and valleys along with the maximum profit, but we can 
        directly keep on adding the difference between the 
        consecutive numbers of the array if the second number 
        is larger than the first one, and at the total 
        sum we obtain will be the maximum profit. 
        """
        res = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                res += prices[i] - prices[i-1]
        return res

    def maxProfit(self, prices: List[int]) -> int:
        # Traverse through given price array 
        n = len(prices)
        i = 0
        res = 0
        while (i < (n - 1)): 
            
            # Find Local Minima 
            # Note that the limit is (n-2) as we are 
            # comparing present element to the next element 
            while ((i < (n - 1)) and (prices[i + 1] <= prices[i])): 
                i += 1
            
            # If we reached the end, break 
            # as no further solution possible 
            if (i == n - 1): 
                break
            
            # Store the index of minima 
            buy = i 
            i += 1
            
            # Find Local Maxima 
            # Note that the limit is (n-1) as we are 
            # comparing to previous element 
            while ((i < n) and (prices[i] >= prices[i - 1])): 
                i += 1
                
            # Store the index of maxima 
            sell = i - 1
            
            res += prices[sell] - prices[buy] 

        return res
    
    def maxProfitRecursion(self, prices: List[int]) -> int:
        # TLA
        # Buy at first - 0
        # Sell at first possible i
        # Run recursion for prices[i+1:]
        ln = len(prices)
        if ln <= 1:
            return 0
        res = 0
        for i in range(0, ln):
            for j in range(i+1, ln):
                if prices[j] <= prices[i]:
                    continue
                profit = prices[j] - prices[i]
                profit += self.maxProfitRecursion(prices[j+1:])
                res = max(res, profit)
        return res

    
if __name__ == '__main__':
    Solution().run()


