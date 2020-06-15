# Valid Anagram
import collections

class Solution:

    def run(self):        
        print(f'{self.isAnagram("m", "l")} expected False')

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        table1 = collections.Counter(s)
        table2 = collections.Counter(t)
        if len(table1) != len(table2):
            return False
        
        for l1 in table1:
            if table1[l1] != table2[l1]:
                return False
        return True

if __name__ == '__main__':
    Solution().run()