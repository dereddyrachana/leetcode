class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        #print("1",left,right,middle)
        while(left <= right): #problem with out of bounds condition
            middle = (left + right)//2
            if(nums[middle] == target):
                print("2",middle)
                return middle
            elif(nums[middle] < target):
                print("3",middle)
                left = middle +1
                print("right",right)
            elif(nums[middle] > target):
                print("4",middle)
                right = middle - 1
                print("left",left)  
        return -1 #if not found
            
