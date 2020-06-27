# Climbing Stairs

class Solution(object):

    def run(self):
        # 1 <= n <= 45
        print(f'{self.climbStairs(1)}  expected 1')
        print(f'{self.climbStairs(2)}  expected 2')
        print(f'{self.climbStairs(3)}  expected 3')
        print(f'{self.climbStairs(4)}  expected 5')
        print(f'{self.climbStairs(5)}  expected 8')
        print(f'{self.climbStairs(6)}  expected 13')
        print(f'{self.climbStairs(7)}  expected 21')
        print(f'{self.climbStairs(35)}  expected 14930352')
        print(f'{self.climbStairs(45)}  expected 1836311903')
        # recursion
        print(f'{self.climbStairsRecursion(1)}  expected 1')
        print(f'{self.climbStairsRecursion(2)}  expected 2')
        print(f'{self.climbStairsRecursion(3)}  expected 3')
        print(f'{self.climbStairsRecursion(4)}  expected 5')
        print(f'{self.climbStairsRecursion(5)}  expected 8')
        print(f'{self.climbStairsRecursion(6)}  expected 13')
        print(f'{self.climbStairsRecursion(7)}  expected 21')
        print(f'{self.climbStairsRecursion(35)}  expected 14930352')
        print(f'{self.climbStairsRecursion(45)}  expected 1836311903')
        # Fibonacci
        print(f'{self.climbStairsFibonacci(45)}  expected 1836311903')


    def climbStairsRecursion(self, n: int) -> int:
        # Recurision
        # Define result for 1 and 2
        # For every n we can start with 1 
        # or we can start with 2
        # For every n result is count(n-1) + count(n-2)
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairsFibonacci(self, n: int) -> int:
        # Define result for 1 
        # For every n we can start with 1 
        # or we can start with 2
        # For every n result is count(n-1) + count(n-2)
        if n == 1:
            return 1
        f = 1
        s = 2
        
        for i in range(3, n+1):
            t = f + s
            f = s
            s = t
        
        return s

    def climbStairs(self, n: int) -> int:
        # Dynamic Programming with tabulation
        # Define result for 1 and 2
        # For every n we can start with 1 
        # or we can start with 2
        # For every n result is count(n-1) + count(n-2)
        if n == 1:
            return 1
        if n == 2:
            return 2
        steps = {}
        steps[0] = 1
        steps[1] = 2
        k = 2
        while k < n:
            steps[k] = steps[k-1] + steps[k-2]
            k += 1
        
        return steps[n-1]

    
if __name__ == '__main__':
    Solution().run()


