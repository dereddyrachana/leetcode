class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        # print(c)
        time = 0
        cnt = 0
        max_heap = [-cnt for cnt in c.values()]
        # print(max_heap)
        heapq.heapify(max_heap)
        q = deque()
        
        while q or max_heap:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(max_heap,q.popleft()[0])
        return time