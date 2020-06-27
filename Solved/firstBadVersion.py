# First Bad Version

from typing import List

k = 55443

def isBadVersion(version):
    return version >= k
    
class Solution(object):

    def run(self):
        print(f'{self.firstBadVersion(44412143)} expected {k}')
        
    def firstBadVersion(self, n: int) -> int:
        # Find 0 <= k <= n, where
        # isBad(k-1) == False and
        # isBad(k) = True
        # Binary search approach
        l = 1
        r = n
        k = 0
        while l < r:
            k = l + (r-l) // 2
            if isBadVersion(k):
                r = k
            else:
                l = k+1
        return l
        
    
if __name__ == '__main__':
    Solution().run()


