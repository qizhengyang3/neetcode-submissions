class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        
        res = 0
        l = 0
        # Process from left to right for bars smaller than or equal to current left
        for r in range(len(height)):
            if height[r] >= height[l]:
                for i in range(l + 1, r):
                    res += height[l] - height[i]
                l = r

        # Process from right to left to handle the remaining peak
        peak = l
        r = len(height) - 1
        for l in range(len(height) - 1, peak - 1, -1):
            if height[l] >= height[r]:
                for i in range(r - 1, l, -1):
                    res += height[r] - height[i]
                r = l

        return res