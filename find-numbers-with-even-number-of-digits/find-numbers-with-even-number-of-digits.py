class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            num = str(num)
            # print(num)
            # print(len(num))
            if int(len(num)) % 2 == 0:
                count += 1
        return count