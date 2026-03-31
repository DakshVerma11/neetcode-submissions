class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            code = '#' + str(len(string)) + '#' + string
            res.append(code)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '#':
                i += 1
                length = 0
                while i < n and s[i] != '#':
                    length = length * 10 + int(s[i])
                    i += 1
                i += 1
                res.append(s[i:i+length])
                i += length
            else:
                i += 1
        return res