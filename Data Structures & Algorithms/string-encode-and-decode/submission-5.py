class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for c in strs:
            res += str(len(c)) + "#" + c
        
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        # 4#neet4#code4#love3#you

        i = 0
        res = []

        while len(s) > i:
            j = i
            
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            i = j + 1 
            j += length+1
            
            res.append(s[i:j])
            
            i = j
        
        return res