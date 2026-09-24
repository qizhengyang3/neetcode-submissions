class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [0]
        stack = []
        res = 0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] + 1 if stack else 0
                width = i - left
                res = max(res, height * width)
            stack.append(i)
        return res









# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         # Append a 0 to force popping all remaining bars at the end
#         heights = heights + [0]
#         stack = []   # stores indices, heights[stack] is increasing
#         res = 0

#         for i, h in enumerate(heights):
#             # Pop taller bars — they can't extend past i
#             while stack and heights[stack[-1]] > h:
#                 height = heights[stack.pop()]
#                 # Left boundary: index after the new stack top (or 0 if empty)
#                 left = stack[-1] + 1 if stack else 0
#                 width = i - left
#                 res = max(res, height * width)
#             stack.append(i)

#         return res