class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ''
        max_len = 0
        for char in s:
            if char not in sub:
                #print(sub)
                sub = sub + char
                max_len = max(len(sub),max_len)
            else:
                cut = sub.index(char)
                sub = sub[cut+1:] + char
        return max_len
            #asdpwehjkrp  
                