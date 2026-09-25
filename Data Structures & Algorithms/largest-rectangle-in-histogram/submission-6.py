class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [0]
        res = 0
        stack = []

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] + 1 if stack else 0
                width = i - left
                res = max(res, height * width)

            stack.append(i)

        return res