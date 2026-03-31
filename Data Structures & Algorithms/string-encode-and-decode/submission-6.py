class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += f"{len(s)}#{s}"
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        
        start, current = 0, 0

        while len(s) > current:
            if s[current] == "#":
                length = int(s[start:current])
                res.append(s[current+1: current+length+1])
                start = current + length + 1
                current = start
            
            current += 1
            
        return res