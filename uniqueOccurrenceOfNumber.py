class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c= Counter(arr)
        s= set()
        for val in c.values():
            if val in s:
                return False
            else:
                s.add(val)
        return True
