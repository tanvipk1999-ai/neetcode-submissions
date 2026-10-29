class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = {} # 1-1,2-2,3-3
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            cnts[n] = 1+cnts.get(n,0)
        for cnt in cnts:
            freq[cnts[cnt]].append(cnt) 
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
                

        
        
        