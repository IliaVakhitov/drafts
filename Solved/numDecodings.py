# Number of decodings with resulted strings

class Solution:
    
    def __init__(self):
        # 97 - a
        # 65 - A
        self.alphabet = {
            i+1: chr(65+i) for i in range(26)
        }

    def run(self):        
        string = '10'
        print(f'{self.numDecodings(string)} - expected 1')
        string = '1123'
        print(f'{self.numDecodings(string)} - expected 5')
        string = '112311'
        print(f'{self.numDecodings(string)} - expected 10')        
        string = '11211'
        print(f'{self.numDecodings(string)} - expected 8')
        string = '1102110'
        print(f'{self.numDecodings(string)} - expected 2')
        string = '112311128'
        print(f'{self.numDecodings(string)} - expected 25')
        # Test cases for leetcode
        """
        string = '11225711258711214262133258'
        print(f'{self.numDecodings(string)} - expected 3840')
        string = '1122571125127112141262133251'
        print(f'{self.numDecodings(string)} - expected 11520')
        string = '11225711251271121412621332511'
        print(f'{self.numDecodings(string)} - expected 23040')
        string = '4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117'
        print(f'{self.numDecodings(string)} - expected 294912')
        string = '475756254584461749455577458134121151129681678658678775525774117859933718648672324752832461211715'
        print(f'{self.numDecodings(string)} - expected 589824')        
        string = '4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948'
        print(f'{self.numDecodings(string)} - expected 589824')
        """

    def encodestring(self, string: str) -> str:
        res = ''
        for l in string:
            res += self.encode(int(l))
        return res

    def encode(self, n: int) -> str:
        return self.alphabet.get(n)

    def combine(self, letters):
        arrays = []
        arrays.append(letters)
        used = [[letters[0]]]
        for i in range(1, len(letters)):        
            l = letters[i]
            add_arr = []
            for arr in used:
                pl = arr[-1]
                if len(l) == 1 and len(pl) == 1 and int(pl+l) < 27:                    
                    add_arr.append(arr[:-1]+[pl+l])
                arr.append(l)    
            for add in add_arr:
                used.append(add)
                arrays.append(add + letters[i+1:])
            
        return arrays

    def numDecodings(self, s: str) -> int:
        dev = False
        encode = True
        if not s:
            return 0
        # started with 0
        string = list(s)
        if string[0] == '0':
            return 0

        letters = []
        # special case is 0
        # we accept 10 and 20 only
        for l in string:
            if l == '0':
                prev = letters.pop()
                if prev != '1' and prev != '2':
                    # invalid string
                    return 0
                letters.append(prev+l)
            else:
                letters.append(l)

        # letters
        if dev:
            print(f'Letters {letters}')

        res = self.combine(letters)
        if dev:
            for string in res:
                print(string)

        resultstrings = str(len(res)) + '\n'
        if encode:
            result = []
            for rstr in res:
                result.append(self.encodestring(rstr))
            
            result.sort()
            for rstr in result:
                resultstrings += rstr + '\n'
        

        return resultstrings


if __name__ == '__main__':
    Solution().run()

