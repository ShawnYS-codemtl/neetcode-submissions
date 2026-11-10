class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + '#' + s
        
        return output
        
    def decode(self, s: str) -> List[str]:
        output = []
        length = ""
        i = 0
        n = len(s)
        start = 0

        if len(s) == 0:
            return output

        while i <= n:
            if s[i] == '#':
                length = int(s[start:i])
                output.append(s[i+1:i+1+length])
                i += 1 + length
                start = i
            i += 1

        return output
