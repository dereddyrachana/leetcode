class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        n = len(height)
        result = 0
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                pop_height = height[stack[-1]]
                stack.pop()
                
                if len(stack) == 0:
                    break
                dist = i - stack[-1] - 1
                min_height = min(height[stack[-1]], height[i]) - pop_height
                
                result += dist * min_height
            
            stack.append(i)
        return result