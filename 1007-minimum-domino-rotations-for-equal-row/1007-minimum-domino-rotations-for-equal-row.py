class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        count_a = defaultdict(int)
        count_b = defaultdict(int)
        N = len(A)
        same = 0

        for i in range(N):
            count_a[A[i]] += 1
            count_b[B[i]] += 1

            if A[i] == B[i]:
                same += 1

        for x in range(1,7):
            if (count_a[x] + count_b[x] - same) == N:
                return N - max(count_a[x], count_b[x])

        return -1