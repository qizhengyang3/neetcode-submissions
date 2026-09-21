class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i != "+" and i != "-" and i != "*" and i != "/":
                stack.append(int(i))
            elif i == "+":
                tmp = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(tmp)
            elif i == "-":
                tmp = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(tmp)
            elif i == "*":
                tmp = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
                stack.append(tmp)
            elif i == "/":
                tmp = int (stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(tmp)
        
        return stack[0] if stack else 0