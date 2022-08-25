class MedianFinder:

    def __init__(self):
        self.small = [] #maxheap
        self.large = [] #minheap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        
        #all num in small < all num in large
        if self.small and self.large and ((-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        #len(small) ~= len(large)
        if(len(self.small) > 1 + len(self.large)):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if(len(self.large) > 1 + len(self.small)):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,-1 * val)
            
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else: 
            return (self.large[0] + (-1 * self.small[0]))/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()