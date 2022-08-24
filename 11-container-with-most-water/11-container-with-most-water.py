class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        area = 0
        right = len(height)-1
        width = right - left
        maxarea = min(height[left],height[right]) * width
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right-=1
            width = right - left
            area = min(height[left],height[right]) * width
            maxarea = max(area,maxarea)
        
        return maxarea
    
            
                
            