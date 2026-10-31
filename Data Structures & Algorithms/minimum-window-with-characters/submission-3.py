class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        min_len = float('inf')
        need = {}
        window = {}

        for c in t:
            need[c] = 1 + need.get(c,0)
        have = 0
        required = len(need)

        l=0
        for r in range(len(s)):
            rc = s[r]
            window[rc] = 1 + window.get(rc,0)

            if rc in need and window[rc] == need[rc]:
                have += 1
            
            while have==required:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    res = s[l:r+1]
                
                window[s[l]] -= 1

                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1

                l+=1
        return res


                
