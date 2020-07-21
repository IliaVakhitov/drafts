# Reverse Integer
from typing import List

class Solution:

    def run(self):        
        print(f'{self.reverse(123)} expected 321')
        print(f'{self.reverse(-123)} expected -321')
        print(f'{self.reverse(120)} expected 21')
        print(f'{self.reverse(0)} expected 0')
        print(f'{self.reverse(1)} expected 1')
        print(f'{self.reverse(10)} expected 1')
        print(f'{self.reverse(100)} expected 1')
        print(f'{self.reverse(1000)} expected 1')
        print(f'{self.reverse(11000)} expected 11')
        print(f'{self.reverse(12000)} expected 21')
        print(f'{self.reverse(-21000)} expected -12')
        print(f'{self.reverse(31000)} expected 13')
        print(f'{self.reverse(1534236469)} expected 0')
    

    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        if -9 < x < 9:
            return x
        mtp = 1
        if x < 0:
            mtp = -1
            x = -x     
        # remove zeros
        while x % 10 == 0:
            x //= 10       
        res = int(str(x)[::-1]) * mtp
        # TODO
        if -2**31 > res or res > 2**31-1:
            return 0
        return res

if __name__ == '__main__':
    Solution().run()