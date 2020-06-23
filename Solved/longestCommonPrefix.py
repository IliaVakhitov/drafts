# Longest Common Prefix

from typing import List

class Solution(object):
    def run(self):
        strings = [
            'aaaacbbc',
            'aaaacddbv',
            'aaaaca'
        ]         
        print(self.longestCommonPrefix(strings)) # 'aa'

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        if len(strs[0]) == 0:
            return ''
        res = ''
        i = 0
        current = ''
        while True:
            for j in range(0,len(strs)):
                if i >= len(strs[j]):
                    return res
                if j == 0:
                    current = strs[j][i]
                    continue
                if strs[j][i] != current:
                    return res
            res += current
            i += 1
        return res   
        
if __name__ == '__main__':
    Solution().run()

