class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sets = set()
        k = 0
        for i in range(0,len(nums)):
            if nums[i] not in sets:
                ele = nums[i]
                sets.add(nums[i])
                nums[k] = ele
                k = k+1
                print(k)
        print("Hi")
        print(nums[:k])
        return k
                
                