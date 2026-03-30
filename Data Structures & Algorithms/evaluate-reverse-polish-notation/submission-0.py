class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ["+","-","*","/"]
        for token in tokens:
            if token in operands:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if token == "+":
                    total = num2 + num1
                elif token == "-":
                    total = num1 - num2
                elif token == "*":
                    total = num1 * num2
                else:
                    total = num1 // num2
                stack.append(total)
            else:
                stack.append(token)
        
        return stack[-1]
