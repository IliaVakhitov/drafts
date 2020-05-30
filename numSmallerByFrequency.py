# Compare Strings by Frequency of the Smallest Character

from typing import List


class Solution:
  
    def run(self):  
        # queries[i][j], words[i][j] are English lowercase letters 
             
        queries = ["cbd"]
        words = ["zaaaz"]
        print(f'{self.numSmallerByFrequency(queries, words)} - expected [1]')
        
        queries = ["bbb","cc"]
        words = ["a","aa","aaa","aaaa"]
        print(f'{self.numSmallerByFrequency(queries, words)} - expected [1,2]')
        
    def func(self, input: str) -> int:
        data = list(input)
        data.sort()
        res = 0
        first = data[0]
        for char in data:
            if char == first:
                res += 1
            else:
                break
        return res


    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        answer = []
        values = {}
        for query in queries:
            res = 0
            fq = self.func(query)            
            for word in words:
                if word in values:
                    fw = values[word]
                else:
                    fw = self.func(word)
                    values[word] = fw
                if fq < self.func(word):
                    res += 1
            answer.append(res)
        return answer  


if __name__ == '__main__':
    Solution().run()

