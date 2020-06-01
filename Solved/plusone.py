class Solution(object):
    def run(self):
        print(f'{self.plusOne([1, 2, 3])} expected [1,2,4]')
        print(f'{self.plusOne([1, 2, 0])} expected [1,2,1]')
        print(f'{self.plusOne([1])} expected [2]')
        print(f'{self.plusOne([0])} expected [1]')
        print(f'{self.plusOne([9])} expected [1,0]')
        print(f'{self.plusOne([9, 9])} expected [1,0,0]')
        print(f'{self.plusOne([1, 0, 0])} expected [1,0,1]')
        print(f'{self.plusOne([9, 9, 9])} expected [1,0,0,0]')
        print(f'{self.plusOne([9, 0, 9])} expected [9,1,0]')

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # end of recursion previous was 9
        if len(digits) == 0:
            digits.append(1)
            return digits
        # take last digit and +1 to it if != 9
        last = digits.pop()
        if last != 9:
            digits.append(last+1)
            return digits
        else:
            # find plus one without last 9
            # insert 0 instead of nine
            res = self.plusOne(digits)
            res.append(0)
            return res

