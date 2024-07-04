class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res= {}

        for s in strs:
            str_sorted= sorted(s)
            key= tuple(str_sorted)
            if key not in res:
                res[key]= [s]
            else:
                res[key].append(s)

        return res.values()
