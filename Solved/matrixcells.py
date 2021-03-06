# Matrix Cells in Distance Order


class Solution(object):
    def run(self):
        print(f'{self.allCellsDistOrder(1,2,0,0)} expected [[0,0],[0,1]]')
        print(f'{self.allCellsDistOrder(2,2,0,1)} expected [[0,1],[0,0],[1,1],[1,0]]')
        print(f'{self.allCellsDistOrder(2,3,1,2)} expected [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]')

        test_res = [[4,6],[3,6],[4,5],[4,7],[5,6],[2,6],[3,5],[3,7],[4,4],[4,8],[5,5],[5,7],[6,6],[1,6],[2,5],[2,7],[3,4],[3,8],[4,3],[4,9],[5,4],[5,8],[6,5],[6,7],[7,6],[0,6],[1,5],[1,7],[2,4],[2,8],[3,3],[3,9],[4,2],[5,3],[5,9],[6,4],[6,8],[7,5],[7,7],[8,6],[0,5],[0,7],[1,4],[1,8],[2,3],[2,9],[3,2],[4,1],[5,2],[6,3],[6,9],[7,4],[7,8],[8,5],[8,7],[9,6],[0,4],[0,8],[1,3],[1,9],[2,2],[3,1],[4,0],[5,1],[6,2],[7,3],[7,9],[8,4],[8,8],[9,5],[9,7],[0,3],[0,9],[1,2],[2,1],[3,0],[5,0],[6,1],[7,2],[8,3],[8,9],[9,4],[9,8],[0,2],[1,1],[2,0],[6,0],[7,1],[8,2],[9,3],[9,9],[0,1],[1,0],[7,0],[8,1],[9,2],[0,0],[8,0],[9,1],[9,0]]
        print(f'{self.allCellsDistOrder(10, 10, 4, 6) == test_res} expected True')

    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        result = [[r0, c0]]
        dist = 0
        while len(result) < R*C:
            dist += 1
            for x in range(dist+1):
                y = dist - x
                if x == 0 and y > 0:
                    if 0 <= c0 - y < C:
                        result.append([r0, c0 - y])
                    if 0 <= c0 + y < C:
                        result.append([r0, c0 + y])
                elif y == 0 and x > 0:
                    if 0 <= r0 - x < R:
                        result.append([r0 - x, c0])
                    if 0 <= r0 + x < R:
                        result.append([r0 + x, c0])
                else:
                    if 0 <= r0 - x < R and 0 <= c0 - y < C:
                        result.append([r0 - x, c0 - y])
                    if 0 <= r0 - x < R and 0 <= c0 + y < C:
                        result.append([r0 - x, c0 + y])
                    if 0 <= r0 + x < R and 0 <= c0 - y < C:
                        result.append([r0 + x, c0 - y])
                    if 0 <= r0 + x < R and 0 <= c0 + y < C:
                        result.append([r0 + x, c0 + y])

        return result


