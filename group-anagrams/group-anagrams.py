class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            if tuple(sorted(word)) not in d:
                d[tuple(sorted(word))] = [word]
            else:
                d[tuple(sorted(word))].append(word)
        print(d)
        return list(d.values())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         d = {}
#         ans = {}
#         for s in strs:
#             d[s] = sorted(list(s))
#         # print(d)
#         for i in strs:
#             if str(d[i]) not in ans:
#                 ans[str(d[i])] = [i]
#                 # print(ans)
#             else:
#                 ans[str(d[i])].append(i)
#         # print(ans)
#         return(list(ans.values()))
        
        
            
        
        
                        
        
            
        