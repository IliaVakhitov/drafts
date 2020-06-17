# Valid Palindrome
import collections

class Solution:

    def run(self):        
        print(f'{self.isPalindrome("")} expected True')
        print(f'{self.isPalindrome("mam")} expected True')
        print(f'{self.isPalindrome("ma")} expected False')
        print(f'{self.isPalindrome("A man, a plan, a canal: Panama")} expected True')

    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i <= j:
            while not s[i].isalnum():                
                i += 1 
                if i >= j:
                    return True
            while not s[j].isalnum():
                j -= 1
                if i >= j:
                    return True
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

if __name__ == '__main__':
    Solution().run()