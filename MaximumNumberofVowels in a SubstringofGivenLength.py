class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        l=len(s)
        ans=cnt= sum(c in vowels for c in s[:k])
        for i in range(k,l):
            cnt += int(s[i] in vowels) - int(s[i-k] in vowels)
            ans =max(ans, cnt)
        return ans

