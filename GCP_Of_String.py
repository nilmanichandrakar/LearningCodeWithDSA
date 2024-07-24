class Solution:
  def gcdOfStrings(self, str1: str, str2: str) -> str:
    def mod(s1: str, s2: str) -> str:
      while s1.startswith(s2):
        s1 = s1[len(s2):]
      return s1

    if len(str1) < len(str2):
      return self.gcdOfStrings(str2, str1)
    if not str1.startswith(str2):
      return ''
    if not str2:
      return str1
    return self.gcdOfStrings(str2, mod(str1, str2))


# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#        if str1 + str2 != str2 + str1:
#         return ""
       
#        from math import gcd
#        return str1[:gcd(len(str1), len(str2))]
