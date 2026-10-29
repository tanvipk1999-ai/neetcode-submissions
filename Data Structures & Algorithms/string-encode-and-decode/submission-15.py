import re
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i))  
            res += "/:"
            res += i
        return res


    def decode(self, s: str) -> List[str]:
        l = []
        if len(s):
            curr = 0
            while curr != len(s):
                s = s[curr:]
                print(s)
                idx = s.find("/:")
                curr = 0
                print(idx)
                l1 = int(s[curr:idx])
                l.append(s[idx+2:idx+2+l1])
                curr = idx+2+l1
                print(s,l)

        return(l)

