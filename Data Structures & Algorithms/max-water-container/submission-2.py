class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = float("-inf")
        maxArea = float("-inf")
        left, right = 0, len(heights) - 1

        while left <= right:
            area = min(heights[left], heights[right]) * (right - left)
            maxArea = max(maxArea, area)

            # we move shorter height b/c we can only get
            # equal or smaller heigh if we move larger height
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea
        