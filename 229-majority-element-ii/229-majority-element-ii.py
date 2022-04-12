class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        arr = []
        dic = {}
        for num in nums:
            if(num not in dic):
                dic[num] = 1
                print("1.", dic)
            elif(num in dic):
                dic[num] = dic[num] + 1
                print(dic)
        for key in dic:
            print("key",key)
            print("h",len(nums)/3)
            print(dic[key])
            if dic[key] > (len(nums)/3):
                arr.append(key)
                
        return arr
            