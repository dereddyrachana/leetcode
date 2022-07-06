class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count_map = dict()
        arr = []
        start_end_map = dict()
        for i in range(0,len(nums)):
            if(nums[i] not in count_map):
                count_map[nums[i]] = 1
                start_end_map[nums[i]] = [i,i]
            else:
                count_map[nums[i]] += 1
                start_end_map[nums[i]][1] = i
        # print(count_map)
        # print(start_end_map)
        val = max(count_map.values())
        for key, value in count_map.items():
            if val == value:
                arr.append(key)
        # print(arr)
        min_val = float('inf')
        for key, value in start_end_map.items():
            if key in arr:
                curr_val = value[1] - value[0] + 1
                if(min_val > curr_val):
                    min_val = curr_val
                    # min_key = key
        return min_val
        