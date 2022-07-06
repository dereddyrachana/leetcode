class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #use a hash map to count the occurances
        hash_map = {}
        for i in range(0,len(arr)):
            if(arr[i] not in hash_map):
                hash_map[arr[i]] = 1
            else:
                hash_map[arr[i]] += 1
        print(hash_map)
        set_values = set()
        for key, value in hash_map.items():
            if value not in set_values:
                set_values.add(value)
            else:
                return False
        return True
        #while adding to the hash map check if the value already exists