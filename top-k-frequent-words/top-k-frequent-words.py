class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for word in words:
            if word not in d:
                d[word] = 1
            else:
                d[word]+=1
        print(d)
        d_sorted = sorted(d.items(), key=lambda x:(-x[1],x[0]))
        
        return [i[0] for i in d_sorted][:k]