class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = [] ## pair tmp index

        for i, tmp in enumerate(temperatures):
            while stack and stack[-1][0] < tmp:
               stackT, stackIndex = stack.pop()
               res[stackIndex] = i - stackIndex 

            stack.append((tmp, i))

        return res