class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs:
            return "-|-".join(strs)
        
        return "__null__"

    def decode(self, s: str) -> List[str]:
        if s == "__null__":
            return []
            
        return s.split("-|-")