# Count and Say


class Solution(object):
    def run(self):
                
        print(self.countAndSay(14))

    def countAndSay(self, n: int) -> str:
        string = '1'
        for i in range(2, n+1):
            string = self.count(string)
        return string

    def count(self, string: str) -> str:
        res = ''
        count = 0
        num = ''
        for i in range(len(string)):
            if num == '' or string[i] == num:
                count += 1
            else:
                res += str(count)
                res += num
                count = 1
            num = string[i]
        res += str(count)
        res += num

        return res
        
if __name__ == '__main__':
    Solution().run()

