class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tmpStack = []
        for c in tokens:
            if c == '+':
                tmpStack.append(tmpStack.pop() + tmpStack.pop())
            elif c == '-':
                a, b = tmpStack.pop(), tmpStack.pop()
                tmpStack.append(b - a)
            elif c == '*':
                tmpStack.append(tmpStack.pop() * tmpStack.pop())
            elif c == '/':
                a, b = tmpStack.pop(), tmpStack.pop()
                tmpStack.append(int(float(b)/a))
            else:
                tmpStack.append(int(c))
        return tmpStack[0]