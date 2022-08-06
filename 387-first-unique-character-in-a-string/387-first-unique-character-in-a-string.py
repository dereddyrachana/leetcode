class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char]+=1
        print
        for char in d:
            if d[char] == 1:
                return s.index(char)
            
        return -1