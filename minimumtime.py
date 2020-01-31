from typing import List


# 10 minutes
class Solution(object):

    def run(self):
        points1 = [[-1, 4], [5, 3], [9, 6], [-3, -7]]
        res = 23
        points2 = [[1,1],[3,4],[-1,0]]
        res = 7
        points3 = [[3, 2], [-2, 2]]
        res = 5
        print(self.minTimeToVisitAllPoints(points1))
        print(self.minTimeToVisitAllPoints(points2))
        print(self.minTimeToVisitAllPoints(points3))

    def minTimeToVisitAllPoints(self, points: List[List[int]]):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total = 0
        for i in range(1, len(points)):
            total += max(abs(points[i][0]-points[i-1][0]), abs(points[i][1]-points[i-1][1]))
        return total


