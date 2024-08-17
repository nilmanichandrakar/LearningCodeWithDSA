class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        l1= len(word1)
        l2= len(word2)
        if l1 != l2:
            return False
        #to check the frequencies
        cnt1= Counter(word1)
        cnt2= Counter(word2)
        return sorted(cnt1.values()) == sorted(cnt2.values()) and set(
            cnt1.keys()) == set(cnt2.keys())
