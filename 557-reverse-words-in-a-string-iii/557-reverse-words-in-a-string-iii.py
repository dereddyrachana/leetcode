class Solution:
    def reverseWords(self, s: str) -> str:
        new = []
        a = s.split(' ')
        # print(a)
        for s in a:
            #print(s)
            new.append(s[::-1])
            #print(new)
        #print(new)
        return " ".join(new)
            
     
            