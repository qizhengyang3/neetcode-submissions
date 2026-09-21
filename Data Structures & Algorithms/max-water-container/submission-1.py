class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while(l < r): 
            tmp_min = min(heights[l], heights[r])
            tmp_res = tmp_min * (r - l)

            res = max(res, tmp_res)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        

        return res

