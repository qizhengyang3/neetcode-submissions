class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        stack = []

        for i in tokens:
            if i == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                temp = num1 + num2
                stack.append(temp)
                
            elif i == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                temp = num2 - num1
                stack.append(temp)
            elif i == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                temp = num1 * num2
                stack.append(temp)
            elif i == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                temp = int(num2 / num1)
                stack.append(temp)
            else:
                stack.append(int(i))
                print(stack[-1])
        
        return stack[0]
        