class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in res_dict:
                res_dict[key].append(s)
            else:
                res_dict[key] = [s]
        return list(res_dict.values())


        