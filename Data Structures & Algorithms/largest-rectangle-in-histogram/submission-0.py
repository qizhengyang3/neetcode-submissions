class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        res = 0

        for i in range(n):
            height = heights[i]

            leftMost = i
            rightMost = i + 1

            while rightMost < n and heights[rightMost] >= height:
                rightMost += 1

            while leftMost >= 0 and heights[leftMost] >= height:
                leftMost -= 1


            rightMost -= 1
            leftMost += 1
            res = max(res, height * (rightMost - leftMost + 1))

        return res
            
