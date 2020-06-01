
class Solution(object):

    def run(self):
        print(str(self.isValid('()')) + ' expected true')
        print(str(self.isValid('(]')) + ' expected false')
        print(str(self.isValid('([]]')) + ' expected false')
        print(str(self.isValid('[(])')) + ' expected false')
        print(str(self.isValid('{()[]}')) + ' expected true')
        print(str(self.isValid('{([])}')) + ' expected true')
        print(str(self.isValid('((((()))))')) + ' expected true')
        print(str(self.isValid('(')) + ' expected fasle')
        print(str(self.isValid(')')) + ' expected false')
        print(str(self.isValid('((((())))))')) + ' expected fasle')
        print(str(self.isValid('')) + ' expected true')

    def isValid(self, s: str) -> bool:
        stack = []
        for next in s:
            if next == '(' or next == '{' or next == '[':
                stack.append(next)
            if not stack and (next == ')' or next == '}' or next == ']'):
                return False

            if next == ')':
                if not stack or stack.pop() != '(':
                    return False

            if next == '}':
                if not stack or stack.pop() != '{':
                    return False
            if next == ']':
                if not stack or stack.pop() != '[':
                    return False
        if stack:
                return False    
        return True
       

if __name__ == '__main__':
    Solution().run()


