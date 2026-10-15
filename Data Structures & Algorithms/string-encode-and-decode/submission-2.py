class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s):03d}")
            encoded += list(s)
        return "".join(encoded)
    def decode(self, s: str) -> List[str]:
        decoded = []
        ptr = 0
        while ptr < len(s):
            # Read length of string
            s_len = int(s[ptr:ptr+3])
            ptr += 3
            decoded.append(s[ptr:ptr+s_len])
            ptr += s_len
        return decoded
