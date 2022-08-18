class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        connected = 0
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        def dfs(i):
            if i not in visited:
                visited.add(i)
                for j in adj[i]:
                    dfs(j)
            
        for i in range(0,n):
            if i not in visited:
                connected+=1
                dfs(i)
            
        return connected
            
            
            
                    
            