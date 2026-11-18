class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        output = 0

        while l < r:
            dist = r - l
            h = min(heights[l], heights[r])
            output = max(output, (dist*h))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return output