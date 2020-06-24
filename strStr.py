# Implement strStr()


class Solution(object):
    def run(self):
        haystack = "hellow"
        needle = "ow"

        print(self.strStr(haystack, needle)) # 2

    def strStr(self, haystack: str, needle: str) -> int:
        # Traverse and search for substring
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        if len(haystack) < len(needle):
            return -1
        if len(haystack) == len(needle) and haystack == needle:
            return 0
        
        lh = len(haystack)
        ln = len(needle)
        for i in range(lh-ln+1):
            if needle == haystack[i:i+ln]:
                return i
        return -1
        
if __name__ == '__main__':
    Solution().run()

