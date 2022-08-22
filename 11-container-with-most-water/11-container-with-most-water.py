class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        #print(p1,p2)
        width = p2-p1
        #print("checking",height[p1],height[p2],width)
        maxarea = min(height[p1], height[p2]) * width
        #print("max=",maxarea)
        while(p2>p1):
            if(height[p1]<height[p2]):
                p1=p1+1
         #       print("p1 moves",p1)
            else:
                p2=p2-1
          #      print("p2 moves",p2)
            width = p2-p1
           # print("width after moving",width)
            #print(height[p1],height[p2])
            area = min(height[p1], height[p2])*width
            #print("area",area)
            if(area>maxarea):
                maxarea = area
             #   print("Yes")
        return maxarea