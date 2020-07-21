# Evaluate Reverse Polish Notation
from typing import List
from math import floor, sqrt

class Solution(object):
    def run(self):

        tokens = ["8","23","8","9","-","-","*"]
        print(self.evalRPN(tokens))

    def evalRPN(self, tokens: List[int]) -> int:
        stack = []
        for token in tokens:    
            if token == "+":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a+b)
                print(stack)
                continue
            if token == "-":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a-b)
                print(stack)
                continue
            if token == "*":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a*b)
                print(stack)
                continue
            if token == "/":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(int(a/b))
                print(stack)
                continue
            stack.append(token)
            print(stack)
        return stack[0]


if __name__ == '__main__':
    Solution().run()
    stack = []

