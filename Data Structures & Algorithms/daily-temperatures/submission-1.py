class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        for l in range(len(temperatures)-2,-1,-1):
            r = l+1
            while r<len(temperatures) and temperatures[r] <= temperatures[l]:
                if res[r] == 0:
                    r = len(temperatures)
                    break
                r += res[r]
            if r<len(temperatures):
                res[l] = r-l
                    
        return res
        