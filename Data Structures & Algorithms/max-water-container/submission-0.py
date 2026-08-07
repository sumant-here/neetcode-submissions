class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights)-1
        mx  = 0 
        while l < r :
            wd = r - l 
            h = min(heights[l],heights[r])
            a = wd * h 
            mx = max(mx,a)
            if heights[l]  < heights[r]:
                l  += 1
            else:
                r -=1
        return mx
