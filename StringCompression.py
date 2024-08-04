class Solution:
    def compress(self, chars: List[str]) -> int:
        w = 0 #write
        r = 0  #read
        n = len(chars)

        while r < n:
            char = chars[r]
            count = 0
            while r< n and chars[r] == char:
                r += 1
                count += 1
           
            chars[w] = char
            w += 1

            if count > 1:
                for digit in str(count):
                    chars[w] = digit
                    w += 1

        return w
