class Solution:
    def sortColors(self, l: List[int]) -> None:
        for i in range(len(l)):
            for j in range(i + 1, len(l)):

                if l[i] > l[j]:
                    l[i], l[j] = l[j], l[i]
        """
        Do not return anything, modify nums in-place instead.
        """
        