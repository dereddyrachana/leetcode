class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","").lower()
        print(s)
        s_new = ''
        for char in s:
            if char.isalnum():
                s_new+=char
        print(s_new)
        return s_new == s_new[::-1]
        
        