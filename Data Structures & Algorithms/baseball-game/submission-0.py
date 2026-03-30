class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for token in operations:
            if token == "+":
                num2 = stack.pop()
                num1 = stack.pop()
                total = num1 + num2
                stack.append(num1)
                stack.append(num2)
                stack.append(total)
            elif token == "D":
                num = stack.pop()
                stack.append(num)
                stack.append(num * 2)
                
            elif token == "C":
                stack.pop()
            else:
                stack.append(int(token))
        return sum(stack)
        