class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        leftMax = heights[l]
        rightMax = heights[r]
        res = 0

        while l < r:
            area = min(leftMax, rightMax) * (r - l )
            res = max(res, area)
            if leftMax < rightMax:
                l += 1
                leftMax = max(heights[l], leftMax)

            else:
                r -= 1
                rightMax = max(rightMax, heights[r])
            
        return res

