class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxf = 0
        l=0
        maxl = 0
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i],0) + 1
            maxf = max(maxf,freq[s[i]])
            while (i-l+1)-maxf >k:
                freq[s[l]] -= 1
                l+=1
            maxl = max(maxl, i-l+1)
        return maxl

            



        