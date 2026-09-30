class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [0]
        res = 0
        stack =[]

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                k = stack.pop()
                height = heights[k]
                left = stack[-1] + 1 if stack else 0
                width = i - left
                res = max(res, width * height)


            stack.append(i)

        return res