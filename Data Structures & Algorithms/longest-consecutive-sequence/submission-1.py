class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        setn = set(nums)
        for i in setn:
            if i-1 not in setn:
                n = i
                length = 0
                while(n in setn):
                    n+=1
                    length += 1
                if length > max_len:
                    max_len = length
        return max_len
                
        
         

        

