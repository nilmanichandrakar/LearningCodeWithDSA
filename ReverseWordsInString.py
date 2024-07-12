class Solution:
    def reverseWords(self, s: str) -> str:
        new_str= ' '.join(s.split(' ')[::-1]).strip(' ')
        res =[]

        for i, c in enumerate(new_str):
            if i< len(new_str) -1 and new_str[i] == new_str[i+1] == ' ':
                i +=1
            else:
                res.append(c)
                i += 1
        
        return ''.join(res)

# minimal sol
  # s = s.split()
  #       n = len(s)
  #       i = 0
  #       j = n-1

  #       while i<j:
  #           s[i],s[j] = s[j],s[i]
  #           i+=1
  #           j-=1
  #       return " ".join(s)
        
