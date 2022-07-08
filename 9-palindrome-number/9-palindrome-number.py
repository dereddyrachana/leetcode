class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if('-' in x):
            return False
        x_rev = x[::-1]
        print(x_rev)
        return(int(x) == int(x_rev))