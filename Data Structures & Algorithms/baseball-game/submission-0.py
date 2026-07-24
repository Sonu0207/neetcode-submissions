class Solution:
    def calPoints(self, operations: List[str]) -> int:
        tempstack = []
        for val in operations:
            if val == "+":
                a, b = tempstack[-1], tempstack[-2]
                tempstack.append(a+b)
            elif val == 'C':
                tempstack.pop()
            elif val == 'D':
                a = tempstack[-1]
                tempstack.append(2*a)
            else:
                tempstack.append(int(val))
        a = 0
        for v in tempstack:
            a += v
        return a