class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(')')
            elif s[i] == '[':
                stack.append(']')
            elif s[i] == '{':
                stack.append('}')

            else:
                if not stack:
                    return False
                if s[i] != stack.pop():
                    return False
        if not stack:
            return True
        else:
            return False