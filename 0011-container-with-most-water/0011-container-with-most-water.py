class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0,len(height) - 1
        area = 0
        while left < right:
            output = (right - left) * min(height[left],height[right])
            area = max(area,output)
         
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
                