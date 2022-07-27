class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = [(char.lower()) for char in s if char.isalnum()]
        print("".join(s_new))
        s_new = "".join(s_new)
        return s_new == s_new[::-1]
        