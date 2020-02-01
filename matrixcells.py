# Matrix Cells in Distance Order
class Solution(object):
    def run(self):
        print(f'{self.allCellsDistOrder(1,2,0,0)} expected [0,1]')
        print(f'{self.allCellsDistOrder(2,2,0,1)} expected [0,1,1,2]')
        print(f'{self.allCellsDistOrder(2,3,1,0)} expected [0,1,1,2,2,3]')

    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
