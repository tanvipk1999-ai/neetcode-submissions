class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = {} #{1-1,2-1,3-3}
        freq = [[]]
        res = []
        for num in nums:
            cnts[num] = 1 + cnts.get(num, 0)
            freq.append([])
        for cnt in cnts:
            freq[cnts[cnt]].append(cnt) #[[],[1,2],[],[3]]
        for i in range(len(freq)-1,0,-1):
            if freq[i]:
                for num in freq[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
                    




        

                
                

        
        
        